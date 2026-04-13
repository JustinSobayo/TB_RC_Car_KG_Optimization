"""
FastAPI application entrypoint.

This file creates the app object that uvicorn runs. It is responsible for:
  1. Cleaning up the Neo4j connection when the app shuts down (lifespan).
  2. Allowing the React frontend to talk to this API (CORS middleware).
  3. Registering the route files so /health and /chat actually exist.

What is already done for you:
  - The FastAPI app with its lifespan (handles Neo4j shutdown).
  - All necessary imports.

What you need to implement:
  - CORS middleware so the frontend (port 5173) can call the backend (port 8000).
  - Router registration so the API endpoints are available.
"""

from contextlib import asynccontextmanager
from multiprocessing.reduction import register

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import chat, health
from app.services.graph_client import close_graph_driver


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    close_graph_driver()


app = FastAPI(
    title="RC Car Graph Chatbot API",
    description="Natural-language chat over Neo4j via Gemini-generated read-only Cypher.",
    lifespan=lifespan,
)


# TODO-4 (Required): Add CORS middleware.
#
# The React frontend runs on http://localhost:5173 but the API runs on
# http://localhost:8000. Browsers block cross-origin requests by default.
# CORS middleware tells the browser "it's okay, let the frontend talk to me."
#
# Call:
#   app.add_middleware(
#       CORSMiddleware,
#       allow_origins=["*"],        # which domains can call us ("*" = any)
#       allow_credentials=True,     # allow cookies/auth headers
#       allow_methods=["*"],        # allow GET, POST, PUT, DELETE, etc.
#       allow_headers=["*"],        # allow any request headers
#   )
#
# In production you'd replace "*" with your actual frontend URL, but for
# local development "*" is fine.


# TODO-5 (Required): Register the route files (routers).
#
# FastAPI uses "routers" to organize endpoints into separate files.
# The health and chat modules each export a `router` object.
# You need to include both so the /health and /chat URLs work.
#
# Call app.include_router() once for each router:
#   app.include_router(health.router)
#   app.include_router(chat.router)
#
# After this, visiting http://localhost:8000/health and POSTing to
# http://localhost:8000/chat will hit the functions in those files.
app.include_router(chat.router)
app.include_router(health.router)