## TODOs ranked by difficulty

This is a rough difficulty guide to help you split work evenly across the team. Assumptions: everyone is comfortable with basic Python/TypeScript; “harder” items usually involve more moving parts, external services, or error handling.

### Easy

- **TODO-1** — `backend/app/models/schemas.py`  - ayira
  Add a `message` field to a Pydantic model.

- **TODO-2** — `backend/app/models/schemas.py` -   Joel
  Add `answer` and `cypher` fields to another Pydantic model.

- **TODO-3** — `backend/app/models/schemas.py`  - Junia
  Add three simple fields to a health response model.

- **TODO-12** — `frontend/src/types/chat.ts`  - Justin
  Define TypeScript types that mirror the backend schemas.

- **TODO-15** — `frontend/src/main.tsx`  - Joel
  Mount the React app into the root DOM node.

- **TODO-16** — `frontend/src/App.tsx`  - Bruno
  Import and render the `ChatLayout` component.

- **TODO-17** — `frontend/src/components/ChatInput.tsx`  - Emily
  Create an input state variable with `useState`.

- **TODO-19** — `frontend/src/components/MessageList.tsx`  - Jovani
  Render a list of messages with simple per-message JSX.

### Medium

- **TODO-4** — `backend/app/main.py`  - Junia
  Add CORS middleware to FastAPI so the frontend can call the API.

- **TODO-5** — `backend/app/main.py`  - Dani
  Register the router files so the `/health` and `/chat` endpoints are live.

- **TODO-6** — `backend/app/api/routes/health.py`  - Dani
  Check Neo4j connectivity and return a `HealthResponse`.

- **TODO-7** — `backend/app/api/routes/chat.py`  - Ayira
  Wrap `run_chat()` in try/except and map errors to HTTP responses.

- **TODO-9** — `backend/app/services/answer_formatter.py`  - Bruno
  Format Neo4j result rows into a user-friendly answer string.

- **TODO-13** — `frontend/src/lib/api.ts`  - Moline
  Implement `sendChat()` to POST to `/chat` and parse the response.

- **TODO-18** — `frontend/src/components/ChatInput.tsx`  - jovani
  Build the submit handler and JSX, wiring up the `onSend` callback.

- **TODO-20** — `frontend/src/components/ChatLayout.tsx`  - Emily
  Manage chat state and implement the `handleSend` function.

- **TODO-21** — `frontend/src/components/ChatLayout.tsx`  - Kaden
  Render the full layout, composing `MessageList` and `ChatInput`.

- **TODO-14** (Optional) — `frontend/src/lib/api.ts`  - Abi
  Implement `getHealth()` to call `/health` and type the response.

### Hard

- **TODO-8** — `backend/app/services/graph_client.py`  - Moline
  Execute Cypher queries via the Neo4j driver and return structured results. 

- **TODO-10** — `backend/app/services/chat_service.py`  - Abi
  Design a good Gemini system prompt that keeps queries safe and on-topic.

- **TODO-11** — `backend/app/services/chat_service.py` - Kaden
  Call the Gemini API, handle possible errors/blocked content, and extract the generated Cypher. 

