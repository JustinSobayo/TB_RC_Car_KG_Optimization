/**
 * frontend/src/App.tsx
 *
 * Top-level React component — the entry point for the UI.
 *
 * What is already done for you:
 *   - main.tsx will render <App />, so this component controls the whole page.
 *
 * What you need to implement:
 *   - Import and render the ChatLayout component.
 */

// TODO-16 (Required): Import ChatLayout and render it.
//
// Steps:
//   1. Import the ChatLayout component:
//        import ChatLayout from "./components/ChatLayout";
//
//   2. Replace the placeholder return below with:
//        return <ChatLayout />;
//
//   Optional: wrap it in a container div with a title/header if you want.

import ChatLayout from "./components/ChatLayout";


export default function App() {
 return (
   <div>
     <h1>Chat App</h1>
     <ChatLayout />
   </div>
 );
}