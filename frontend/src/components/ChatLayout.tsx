/**
 * frontend/src/components/ChatLayout.tsx
 *
 * Main chat page layout — manages message state and wires child components.
 */

import { useState } from "react";
import MessageList, { type Message } from "./MessageList";
import ChatInput from "./ChatInput";

const BASE_URL = "http://localhost:8000";

export default function ChatLayout() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleSend(message: string) {
    setMessages((prev: Message[]) => [...prev, { role: "user", text: message }]);
    setLoading(true);
    try {
      const res = await fetch(`${BASE_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      if (!res.ok) {
        const errText = await res.text();
        throw new Error(errText || res.statusText);
      }
      const data = (await res.json()) as { answer: string };
      setMessages((prev: Message[]) => [...prev, { role: "bot", text: data.answer }]);
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setMessages((prev: Message[]) => [
        ...prev,
        { role: "bot", text: `Error: ${msg}` },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="chat-layout">
      <h1>RC Car Graph Chatbot</h1>
      <MessageList messages={messages} />
      <ChatInput onSend={handleSend} disabled={loading} />
    </div>
  );
}
