import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "./App.css";
import ChatScreen from "./components/ChatScreen";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/chat/case1" />} />
        <Route path="/chat/:caseId" element={<ChatScreen />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
