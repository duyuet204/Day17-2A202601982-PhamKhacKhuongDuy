# Lab 17 Submission — Multi-Memory Agent with Zep

## 1. Thực hành: Phân tích Memory System

### Câu 1: Layer quan trọng nhất trong bộ test

**Long-term memory** là layer quan trọng nhất vì nó phục vụ nhiều case nhất (E02, E03, E08, E09) và chứa thông tin cross-session mà không layer nào khác có. Không có long-term, agent không biết Minh thích Python hay Lan dùng Java/Spring Boot — toàn bộ personal context biến mất sau khi thread kết thúc.

### Câu 2: Trade-off Context Block / Zep vs Redis + Qdrant

| Tiêu chí | Zep Cloud (managed) | Redis + Qdrant (self-hosted) |
|---|---|---|
| Triển khai | SDK đơn giản, không cần infra | Cần vận hành 2 service riêng |
| Semantic search | Tích hợp sẵn graph + vector | Phải tự sync Redis ↔ Qdrant |
| Context Block | Tự động, priority + recency | Phải tự implement ranking |
| Cross-session recall | Native user graph | Phải tự query + merge |
| Latency | Cloud API call | Local nhưng cần 2 lần round-trip |

**Kết luận:** Zep phù hợp khi muốn đánh đổi chi phí cloud để lấy integration nhanh, structured context block, và provenance tracking tự động. Redis+Qdrant phù hợp khi cần kiểm soát hoàn toàn dữ liệu và có team infra sẵn sàng vận hành.

### Câu 3: Guardrail chống Memory Poisoning

Ba guardrail chính:
1. **Consent gate:** Mọi message chỉ được ingest khi user có `memory_opt_in = true` trong `consent.json`. Không opt-in = không ingest.
2. **PII minimization:** Email, phone, địa chỉ bị redact trong `minimize_pii()` trước khi gửi lên Zep. Poisoned input bị sanitize ngay tại source.
3. **Right to be Forgotten:** `src.forget` xóa user khỏi Zep + Redis. Không có cơ chế delete, poisoned memory tồn tại mãi mãi.

## 2. Phân tích Benchmark

### Câu 1: Layer nào có hit rate thấp nhất?

Không có layer nào thấp — memory-enabled đạt **100%** across all layers. Tuy nhiên, trong no-memory baseline, **long-term, episodic, semantic đều 0%** vì không có durable memory. Short-term giữ được 50% (2/2) nhờ dữ liệu còn trong thread.

### Câu 2: Query nào retrieve nhiều token nhất?

**E08** (BLUEBIRD-42 backend stack) retrieve 1495 tokens — cao nhất trong bộ test. Nguyên nhân: query về project constraint kéo theo toàn bộ user summary, tất cả facts về BLUEBIRD-42/TypeScript/NestJS, và episodes liên quan đến async debugging của Minh.

### Câu 3: E07 (mixed) cần kết hợp memory nào?

E07 yêu cầu **long-term + semantic**. Evidence bắt buộc là `Python` (preference cá nhân của Minh, từ long-term) và `Idempotency-Key` (payment retry policy, từ semantic domain KB). Thiếu một trong hai → FAIL.

### Câu 4: Token reduction không đồng nghĩa hit rate cao?

**Đúng.** No-memory baseline có token reduction **81.8%** (cao nhất!) nhưng hit rate chỉ **18.2%** vì nó retrieve gần như nothing. Token reduction cao chỉ có nghĩa khi đi kèm hit rate cao — tức là "giữ đúng thứ, bỏ đúng thứ." Memory-enabled giảm 14.2% nhưng đạt 100% hit rate → retrieval thông minh hơn, không phải retrieval ít hơn.

## 3. Summary

| Metric | Memory-enabled | No-memory |
|---|:---:|:---:|
| Hit rate | **100%** | 18.2% |
| Passed | **11/11** | 2/11 |
| Avg latency (ms) | 866.2 | 0.0 |
| Token reduction | 14.2% | 81.8% |
