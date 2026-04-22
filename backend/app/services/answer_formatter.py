"""
Turn Neo4j record dicts into short human-readable text for the chat UI.

What is already done for you:
  - The function signature and the empty-results case.
  - The json import for formatting.

What you need to implement:
  - Handle a single-value result (1 row, 1 column) → return "key: value".
  - Handle small result sets (≤10 rows) → return a formatted JSON summary.
  - Handle large result sets (>10 rows) → return a count + first few rows.
"""

from __future__ import annotations

import json

def format_graph_results(records: list[dict]) -> str:
   """Convert a list of Neo4j record dicts into a user-friendly string."""


   if not records:
       return "No matching data was found in the graph for that question."


   # TODO-9 (Required): Format the results based on how many rows came back.
   #
   # Handle three cases:
   #
   # Case A — Single value (1 row with 1 key):
   #   Return a string like "key: value"
   #   Hint: use next(iter(records[0].items())) to get the key and value.
   #
   # Case B — Small result set (≤10 rows):
   #   Return "Results (N row(s)):\n" followed by pretty-printed JSON.
   #   Hint: json.dumps(records, indent=2, default=str)
   #
   # Case C — Large result set (>10 rows):
   #   Return "Found N rows. First rows: " followed by the first 5 rows as JSON.
   #   Hint: json.dumps(records[:5], default=str)


   if not records:
       return "No matching data was found in the graph for that question."
  
   if len(records) == 1 and len(records[0]) == 1:
       key, value = next(iter(records[0].items()))
       return f"{key}: {value}"
  
   if len(records) <= 10:
       formatted_json = json.dumps(records, indent=2, default=str)
       return f"Results ({len(records)} row(s)):\n{formatted_json}"
  
   preview_json = json.dumps(records[:5], default=str)
   return f"Found {len(records)} rows. First rows:\n{preview_json}"