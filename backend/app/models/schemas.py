"""
Pydantic request/response models for the HTTP API.

These classes define the exact shape of JSON that the API accepts and returns.
FastAPI uses them automatically for validation and documentation.

What is already done for you:
  - The class names and base class (BaseModel) for each schema.
  - Imports for Pydantic's BaseModel and Field.

What you need to implement:
  - The fields inside each model so FastAPI knows what data to expect.

Reference:
  - Pydantic docs: https://docs.pydantic.dev/latest/concepts/models/
  - Field(...) means "required" — the caller must provide it.
  - Field(default=...) means "optional" — a default is used if omitted.
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    # TODO-1 (Required): Add a field called `message`.
    #
    # This is the user's question (e.g. "How many sessions are in the graph?").
    # It should be:
    #   - type: str
    #   - required (use ... as the default in Field)
    #   - minimum length of 1 (so empty strings are rejected)
    #
    # Syntax:
    #   field_name: type = Field(default, min_length=..., description="...")
    #
    # Example of a required string field with min length:
    #   name: str = Field(..., min_length=1, description="The person's name")
    pass


class ChatResponse(BaseModel):
    # TODO-2 (Required): Add two fields — `answer` and `cypher`.
    #
    # `answer` — the human-readable response shown in the chat UI.
    #   - type: str
    #   - required
    #
    # `cypher` — the generated Cypher query (shown for debugging/teaching).
    #   - type: str or None  (written as: str | None)
    #   - optional, default to None
    #
    # Example of an optional nullable field:
    #   debug_info: str | None = Field(default=None, description="Extra info")
    pass


class HealthResponse(BaseModel):


  status:str = "ok"
  neo4j: str = "unknown"
  gemini_configured: bool = False

    # TODO-3 (Required): Add three fields — `status`, `neo4j`, and `gemini_configured`.
    #
    # `status` — overall API health, default "ok"
    #   - type: str, default: "ok"
    #
    # `neo4j` — connection state of the graph database, default "unknown"
    #   - type: str, default: "unknown"
    #
    # `gemini_configured` — whether the LLM API key is set, default False
    #   - type: bool, default: False
    #
    # For fields with defaults you don't need Field(...), just use =
    #   Example: status: str = "ok"
    #   Or with description: status: str = Field(default="ok", description="...")
