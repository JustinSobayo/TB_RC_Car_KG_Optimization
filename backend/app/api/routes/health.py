"""
Health-check endpoint for quick diagnostics.

This endpoint lets you (and Docker) verify that the API is running and
that it can reach Neo4j and has a Gemini key configured.

What is already done for you:
  - The router, route decorator, and all imports.
  - get_graph_client() to test Neo4j, get_settings() for config values.

What you need to implement:
  - The body of get_health() that checks each dependency and returns
    a HealthResponse with the results.
"""

from fastapi import APIRouter

from app.core.config import get_settings
from app.models.schemas import HealthResponse
from app.services.graph_client import get_graph_client

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    # TODO-6 (Required): Check Neo4j connectivity and return a HealthResponse.
    #
    # Steps:
    #   1. Load settings:
    #        settings = get_settings()
    #
    #   2. Try to verify Neo4j is reachable:
    #        - Call get_graph_client().verify_connectivity()
    #        - If it succeeds → neo4j_status = "ok"
    #        - If it raises any Exception → neo4j_status = "error"
    #        Use a try/except block for this.
    #
    #   3. Determine the overall status:
    #        - "ok" if neo4j_status is "ok"
    #        - "degraded" otherwise
    #
    #   4. Check if Gemini is configured:
    #        bool(settings.gemini_api_key.strip())
    #        This returns True if the key is set, False if empty.
    #
    #   5. Return a HealthResponse with all three values:
    #        return HealthResponse(
    #            status=...,
    #            neo4j=...,
    #            gemini_configured=...,
    #        )

settings = get_settings()
try:
    get_graph_client().verify_connectivity()
    neo4j_status = "ok"
except Exception:
   neo4j_status = "error"
if neo4j_status == "ok":
    overall_status = "ok"
else:
    overall_status = "degraded"
gemini_configured=bool(settings.gemini_api_key.strip())
return HealthResponse(
    status=overall_status,
    neo4j=neo4j_status,
    gemini_configured=gemini_configured,
)