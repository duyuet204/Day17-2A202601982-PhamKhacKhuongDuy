# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1439.4 ms**
- Average token reduction vs full source context: **14.4%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 2944.1 | 823 | 0.0% |  |
| G09 | semantic | PASS | 302.8 | 56 | 87.8% |  |
| G10 | semantic | PASS | 297.8 | 87 | 81.0% |  |
| G14 | mixed | PASS | 2251.8 | 383 | 1.0% |  |
| G03 | long_term | PASS | 1829.9 | 1555 | 0.0% |  |
| G04 | long_term | PASS | 1832.5 | 1536 | 0.0% |  |
| G07 | episodic | PASS | 294.2 | 274 | 0.0% |  |
| G08 | episodic | PASS | 320.1 | 292 | 0.0% |  |
| G11 | mixed | PASS | 2734.9 | 428 | 24.2% |  |
| G13 | mixed | PASS | 606.2 | 515 | 8.8% |  |
| G15 | mixed | PASS | 2327.0 | 922 | 0.0% |  |
| G16 | mixed | PASS | 2139.6 | 429 | 24.1% |  |
| G17 | mixed | PASS | 1836.6 | 429 | 24.1% |  |
| G18 | mixed | PASS | 604.0 | 696 | 0.0% |  |
| G19 | mixed | PASS | 2053.7 | 965 | 0.0% |  |
| G05 | long_term | PASS | 1732.3 | 1635 | 0.0% |  |
| G12 | mixed | PASS | 2437.6 | 423 | 33.1% |  |
| G20 | mixed | PASS | 2242.2 | 605 | 4.3% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> Lan Tran is working on the LOTUS-88 project, prioritizing Java and Spring Boot for backend development.  Lan Tran prioritizes Java and Spring Boot for backend development and explicitly avoids using Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Cont`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### G10 - semantic

`EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.","source":"lab-design-note","updated_at":"2026-08-13T00:00:00Z"} metadata=`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan Tran is working on the LOTUS-88 project, prioritizing Java and Spring Boot for backend development.  Lan Tran prioritizes Java and Spring Boot for backend development and explicitly avoids using Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: mess`

### G03 - long_term

`<USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short code exampl`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short code exampl`

### G07 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Ten du an ca nhan cua toi la ORCHI`

### G08 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connect`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short`

### G13 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Mai hop mentor, toi nay minh muon don open-loop. Liet ke viec chua dong, deadline, va ma dinh da`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short`

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Mai hop mentor, toi nay minh muon don open-loop. Liet ke viec chua dong, deadline, va ma dinh da`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short code exampl`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They need to complete a benchmark report for an open loop called LAB-REPORT-1600 before Saturday at 4:00 PM. The user is currently debugging async HTTP requests related to connection churn, specifically identifying ASYNC-FIX-20. They have found that reusing the aiohttp ClientSession and setting concurrency to 20 is an effective approach. Increasing the timeout did not resolve the connection churn issue.  The user prefers Python and dislikes Java, favoring short`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
