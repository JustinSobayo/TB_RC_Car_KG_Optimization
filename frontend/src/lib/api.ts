/**
 * frontend/src/lib/api.ts
 *
 * Central API client functions used by frontend components to talk to the backend.
 *
 * What is already done for you:
 *   - The file structure and the backend base URL constant.
 *
 * What you need to implement:
 *   - A sendChat() function that POSTs a question to /chat.
 *   - An optional getHealth() function that GETs /health.
 */

import type { ChatRequest, ChatResponse } from "../types/chat";

const BASE_URL = "http://localhost:8000";

// TODO-13 (Required): Implement sendChat().
//
// This function should:
//   1. Accept a `message` string parameter.
//   2. Send a POST request to `${BASE_URL}/chat` with:
//      - Header: "Content-Type": "application/json"
//      - Body: JSON.stringify({ message })      ← this matches ChatRequest
//   3. Check if the response is ok (response.ok). If not, throw an Error
//      with the status text or parsed error detail.
//   4. Parse the JSON response and return it as ChatResponse.
//
// Signature:
//   export async function sendChat(message: string): Promise<ChatResponse> { ... }
export async function sendChat(message: string): Promise<ChatResponse> {
    try {
        const response = await fetch(`${BASE_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type" : "application/json",
            },
            body: JSON.stringify({ message }),
        });
        if (!response.ok) {
            let errorText: string;
            try {
                const errorData = await response.json();
                errorText = errorData.detail || response.statusText;
            } catch {
                errorText = response.statusText;
            }
            throw new Error(`Chat request failed: ${errorText}`);
        }
        const data: ChatResponse = await response.json();
        return data;
    } catch (err) {
        throw new Error(`sendChat error: ${(err as Error).message}`);
    }
}

// TODO-14 (Optional): Implement getHealth().
//
// This function should:
//   1. Send a GET request to `${BASE_URL}/health`.
//   2. Parse and return the JSON response.
//
// Signature:
//   export async function getHealth(): Promise<{ status: string; neo4j: string; gemini_configured: boolean }> { ... }

export async function getHealth(): Promise<{
	status: string;
	neo4j: string;
	gemini_configured: boolean;
}> {
	const res = await fetch(`${BASE_URL}/health`);
	if (!res.ok) {
		// Try to surface a helpful error message from the backend if available
		try {
			const err = await res.json();
			throw new Error(err.detail || err.message || res.statusText);
		} catch (e) {
			throw new Error(res.statusText || "Health check failed");
		}
	}

	const data = await res.json();
	// Cast to the expected shape; backend owns the canonical schema
	return data as { status: string; neo4j: string; gemini_configured: boolean };
}
