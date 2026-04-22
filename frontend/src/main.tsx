/**
 * frontend/src/main.tsx
 *
 * React entry point — mounts the app into the DOM.
 *
 * What is already done for you:
 *   - The HTML page (index.html) has a <div id="root"></div> waiting for React.
 *
 * What you need to implement:
 *   - Import React, ReactDOM, and your App component.
 *   - Create a React root and render <App /> into it.
 */

// TODO-15 (Required): Mount the React app.
//
// Steps:
//   1. Import React and ReactDOM:
//        import React from "react";
//        import ReactDOM from "react-dom/client";
//
//   2. Import your App component:
//        import App from "./App";
//
//   3. Find the root element and create a React root:
//        const rootElement = document.getElementById("root")!;
//        const root = ReactDOM.createRoot(rootElement);
//
//   4. Render the App:
//        root.render(
//          <React.StrictMode>
//            <App />
//          </React.StrictMode>
//        );
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const rootElement = document.getElementById("root")!;
const root = ReactDOM.createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
); 