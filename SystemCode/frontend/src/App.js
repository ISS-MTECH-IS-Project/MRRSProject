import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "./App.css";
import ChatScreen from "./components/ChatScreen";
import CreateCase from "./components/CreateCase";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CreateCase />} />
        <Route path="/chat/:caseId" element={<ChatScreen />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
