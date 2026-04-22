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
    message: str = Field(default=..., min_length=1, description="The user's question")

class ChatResponse(BaseModel):
    # TODO-2 (Required): Add two fields — `answer` and `cypher`.
answer: str = Field(description="The human-readable response shown in the chat UI.")
cypher: str | None = Field(default=None, description="The generated Cypher query (shown for debugging/teaching).")
    pass


class HealthResponse(BaseModel):


  status:str = "ok"
  neo4j: str = "unknown"
  gemini_configured: bool = False

    # TODO-3 (Required): Add three fields — `status`, `neo4j`, and `gemini_configured`.
    status: str = Field(default="ok", description="Overall API health status")
    neo4j: str = Field(default="unknown", description="Connection state of the graph database")
    gemini_configured: bool = Field(default=False, description="Whether the LLM API key is set")
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
