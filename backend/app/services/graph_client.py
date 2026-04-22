"""
Neo4j driver wrapper: connect and run parameterized Cypher.

The _GraphClient class uses a singleton driver pattern — one connection
pool is shared across the whole app regardless of how many requests come in.

What is already done for you:
  - The driver initialization (singleton pattern in __init__).
  - verify_connectivity() for health checks.
  - close_graph_driver() for shutdown cleanup.

What you need to implement:
  - run_query() — execute a Cypher string against Neo4j and return the rows.
"""

from __future__ import annotations

from neo4j import Driver, GraphDatabase

from app.core.config import get_settings

_driver: Driver | None = None


def get_graph_client() -> "_GraphClient":
    return _GraphClient()


class _GraphClient:
    """Thin facade over a singleton driver (one pool per process)."""

    def __init__(self) -> None:
        global _driver
        if _driver is None:
            s = get_settings()
            _driver = GraphDatabase.driver(
                s.neo4j_uri,
                auth=(s.neo4j_username, s.neo4j_password),
            )

    def verify_connectivity(self) -> None:
        assert _driver is not None
        _driver.verify_connectivity()

    def run_query(self, query: str, parameters: dict | None = None) -> list[dict]:
        assert _driver is not None
        parameters = parameters or {}

        rows: list[dict] = []
        with _driver.session() as session:
            result = session.run(query, parameters)
            for record in result:
                rows.append(record.data())
        return rows


def close_graph_driver() -> None:
    global _driver
    if _driver is not None:
        _driver.close()
        _driver = None
