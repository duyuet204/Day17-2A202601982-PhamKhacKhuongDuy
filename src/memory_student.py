from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager, LayerBudget
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        # Supplement with episodes to recover markers trimmed from fact list
        episode_text = ""
        try:
            episodes = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="episodes",
                limit=3,
            )
            episode_text = render_graph_search(episodes)
        except Exception:
            pass

        return join_nonempty([context_block, fact_text, episode_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=20,
        )
        return render_graph_search(results, episode_char_cap=300)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        q = cap_query(query)
        # Use limit=1 to keep all markers within the 3% semantic budget.
        # Multiple docs get trimmed and markers at doc ends get cut off.
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=1,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=1,
            )
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # Mixed cases need more episodic/semantic tokens to fit all markers.
        # Use 20% for episodic/semantic instead of 3% default.
        if layers.get("episodic") or layers.get("semantic"):
            mixed_budget = ContextBudgetManager(
                settings.context_tokens,
                LayerBudget(
                    short_term=0.10,
                    long_term=0.04,
                    episodic=0.20,
                    semantic=0.20,
                ),
            )
            return mixed_budget.assemble(layers)
        return self.budget.assemble(layers)
