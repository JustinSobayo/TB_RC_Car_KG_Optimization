/**
 * frontend/src/components/ChatInput.tsx
 *
 * Captures the user's chat message and triggers a send action.
 *
 * What is already done for you:
 *   - The component signature with an onSend prop.
 *
 * What you need to implement:
 *   - A controlled text input and a submit button.
 *   - Calling onSend() with the current input when the user submits.
 */

import { useState } from "react";

interface ChatInputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

export default function ChatInput({ onSend, disabled }: ChatInputProps) {
  // TODO-17 (Required): Create a state variable for the input text.
  //
  // Use React's useState hook:
  const [input, setInput] = useState("");

  // TODO-18 (Required): Build the submit handler and the JSX.
  //
  // Steps:
  //   1. Write a handleSubmit function that:
  //      - Prevents the default form submit behavior (e.preventDefault()).
  //      - Checks that the input is not empty (after trimming whitespace).
  //      - Calls onSend(input.trim()) to send the message to the parent.
  //      - Clears the input field back to "".
  //
  //   2. Return a <form> that calls handleSubmit on submit, containing:
  //      - An <input> (type="text") bound to the state variable.
  //        Set its value={input}, onChange updates the state,
  //        and disabled={disabled} to block typing while loading.
  //      - A <button> (type="submit") labeled "Send", also disabled={disabled}.
  //
  // Example structure:
  //   return (
  //     <form onSubmit={handleSubmit}>
  //       <input type="text" value={...} onChange={...} disabled={disabled}
  //              placeholder="Ask a question..." />
  //       <button type="submit" disabled={disabled}>Send</button>
  //     </form>
  //   );

  return <div>Chat input not implemented yet</div>;
}
