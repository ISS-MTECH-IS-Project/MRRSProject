import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import Topbar from "./Topbar";
import Messages from "./Messages";

// message : {isSend, isUser, nextOpen, symptoms, diseases, time, body}
const ChatScreen = () => {
  const [messages, setMessages] = useState([]);
  const [isOpen, setOpen] = useState(true);
  let params = useParams();
  const caseId = params.caseId;

  useEffect(() => {
    const getMessages = async () => {
      const caseDetail = await fetchCase(caseId);
      setMessages(caseDetail.messages);
    };

    getMessages();
  }, []);

  // Fetch case
  const fetchCase = async (id) => {
    const res = await fetch(`http://localhost:5000/cases/${id}`, {
      mode: "cors",
    });
    const data = await res.json();
    return data;
  };

  // get next message
  const getGuidedNext = async () => {
    const m = messages[messages.length - 1];
    const res = await fetch(`http://localhost:5000/cases/${caseId}/guided`, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(m),
    });
    const data = await res.json();
    setOpen(data.nextOpen);
    setMessages([...messages, data]);
  };

  // get next message
  const getOpenNext = async (message) => {
    setMessages([...messages, message]);
    const res = await fetch(`http://localhost:5000/cases/${caseId}/open`, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(message),
    });
    const data = await res.json();
    setOpen(data.nextOpen);
    setMessages([...messages, data]);
  };

  const sendMessage = async (message) => {
    if (isOpen) {
      getOpenNext(message);
    } else {
      getGuidedNext();
    }
  };

  // Toggle Reminder
  const toggleConfirm = (mIndex, sIndex) => {
    messages[mIndex].symptoms[sIndex].confirmed =
      !messages[mIndex].symptoms[sIndex].confirmed;
    setMessages(messages);
  };
  // https://www.chatbot.com/chatbot-templates/
  return (
    <div id="widget-global-screen">
      <div dir="ltr" class="lc-main row">
        <div class="col-md-4" />
        <div class="lc-chatbot col-md-4">
          <Header caseId={caseId} />
          <Topbar />
          <Messages messages={messages} onToggle={toggleConfirm} />
          <Footer open={isOpen} onSend={sendMessage} />
        </div>
        <div class="col-md-4" />
      </div>
    </div>
  );
};

export default ChatScreen;
