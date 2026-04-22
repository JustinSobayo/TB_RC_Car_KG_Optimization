"""
Chat orchestration: Gemini generates read-only Cypher → Neo4j → formatted answer.

Requires GEMINI_API_KEY (or GOOGLE_API_KEY) from Google AI Studio.

What is already done for you:
  - Imports, config loading, Cypher extraction/validation helpers.
  - The run_chat() function that ties everything together.

What you need to implement:
  - The system instruction (prompt) that tells Gemini how to behave.
  - The actual Gemini API call that sends the user's question and gets Cypher back.
"""

from __future__ import annotations

import re

import google.generativeai as genai

from app.core.config import get_settings
from app.models.schemas import ChatResponse
from app.services.answer_formatter import format_graph_results
from app.services.graph_client import get_graph_client

_FORBIDDEN_CYPHER = re.compile(
    r"\b(CREATE|MERGE|DELETE|DETACH|SET|REMOVE|DROP|FOREACH)\b",
    re.IGNORECASE,
)


def extract_cypher(raw: str) -> str:
    """Strip optional ```cypher fences from model output."""
    text = raw.strip()
    match = re.search(r"```(?:cypher)?\s*([\s\S]*?)```", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text


def assert_read_only_cypher(cypher: str) -> None:
    """Raise ValueError if the Cypher contains write operations."""
    if _FORBIDDEN_CYPHER.search(cypher):
        msg = "Refusing to run Cypher that may modify the graph (write operations are blocked)."
        raise ValueError(msg)


def generate_cypher(message: str) -> str:
    """Send the user's question to Gemini and get back a Cypher query string."""
    settings = get_settings()
    api_key = settings.gemini_api_key.strip()
    if not api_key:
        raise ValueError(
            "Gemini is not configured. Create a key in Google AI Studio and set GEMINI_API_KEY "
            "(or GOOGLE_API_KEY) in .env. See .env.example."
        )

    genai.configure(api_key=api_key)

    # TODO-10 (Required): Write the system_instruction string.
    #
    # This string is the "system prompt" — it tells Gemini what role it plays
    # and what rules to follow. Your instruction should include:
    #
    #   1. Tell Gemini it is a Neo4j Cypher assistant.
    #   2. Tell it to output ONLY a single Cypher query (nothing else).
    #   3. List the READ-ONLY Cypher clauses it may use:
    #      MATCH, OPTIONAL MATCH, RETURN, WHERE, WITH, ORDER BY, LIMIT, SKIP,
    #      UNWIND, COUNT, collect, DISTINCT, CASE.
    #   4. Explicitly forbid write clauses:
    #      CREATE, MERGE, DELETE, SET, REMOVE, DROP, FOREACH.
    #   5. Include the graph schema from settings so Gemini knows the node labels
    #      and relationship types. Access it via: settings.graph_schema
    #
    # Assign the result to a variable called `system_instruction`.
    #
    # Example skeleton:
    #   system_instruction = (
    #       "You are a ... Output ONLY ... "
    #       "Use these clauses: ... "
    #       "Do NOT use: ... "
    #       f"Graph schema:\n{settings.graph_schema.strip()}"
    #   )

    system_instruction = (
        "You are a Neo4j Cypher assistant. Your sole task is to produce exactly ONE syntactically valid, read-only Cypher query that answers the user's question using the provided graph schema.\n"
        "Output rules (MANDATORY):\n"
        "- Output ONLY a single Cypher query as plain text. Do NOT include any explanation, commentary, backticks, JSON, or other text.\n"
        "- Do NOT output multiple statements or separate queries (no semicolons).\n"
        "- Use ONLY the following read-only clauses: MATCH, OPTIONAL MATCH, RETURN, WHERE, WITH, ORDER BY, LIMIT, SKIP, UNWIND, COUNT, collect, DISTINCT, CASE.\n"
        "- Do NOT use any write or administrative clauses or procedures: CREATE, MERGE, DELETE, SET, REMOVE, DROP, FOREACH, CALL, apoc.*, db.* or other DB admin commands.\n"
        "- If the question cannot be answered from the graph, return a harmless read-only query that returns no rows (for example: RETURN NULL AS _ LIMIT 0). Do not invent facts.\n"
        "- Ensure the query is concise and only references node labels and relationship types present in the provided schema.\n"
        "- Do not assume access to external services or non-standard procedures.\n"
        "Graph schema (use this to decide labels and relationship names):\n"
        f"{settings.graph_schema.strip()}\n"
    )

    model = genai.GenerativeModel(
        model_name=settings.gemini_model,
        system_instruction=system_instruction,
    )

    # TODO-11 (Required): Call model.generate_content() and extract the text.
    #
    # Steps:
    #   1. Call model.generate_content() with the user's `message`.
    #      Pass generation_config=genai.GenerationConfig(temperature=0.1)
    #      to keep output deterministic.
    #   2. Get the text from the response: response.text
    #      (this may raise ValueError if the response was blocked — catch it
    #       and raise a new ValueError with a helpful message).
    #   3. If the text is empty, raise ValueError("Gemini returned an empty response.")
    #   4. Pass the text through extract_cypher() to strip markdown fences.
    #   5. Return the clean Cypher string.
    #
    # Hint:
    #   response = model.generate_content(message, generation_config=...)
    #   content = response.text  # may throw ValueError if blocked

    response = model.generate_content(
        message,
        generation_config=genai.GenerationConfig(temperature=0.1),
    )

    try:
        content = response.text
    except ValueError as exc:
        raise ValueError(
            "Gemini did not return text output (the response may have been blocked by safety "
            "filters). Please rephrase your question and try again."
        ) from exc

    if not content or not content.strip():
        raise ValueError("Gemini returned an empty response.")

    return extract_cypher(content)


def run_chat(message: str) -> ChatResponse:
    """Full chat pipeline: question → Cypher → Neo4j → formatted answer."""
    cypher = generate_cypher(message)
    assert_read_only_cypher(cypher)
    graph = get_graph_client()
    records = graph.run_query(cypher)
    answer = format_graph_results(records)
    return ChatResponse(answer=answer, cypher=cypher)
