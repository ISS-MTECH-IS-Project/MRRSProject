import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import Topbar from "./Topbar";
import Messages from "./Messages";
import Symptom from "./Symptom";
import Disease from "./Disease";
import { Box, Grid } from "@mui/material";
import Paper from "@mui/material/Paper";
import Divider from "@mui/material/Divider";

// message : {isSend, isUser, nextOpen, symptoms, diseases, time, body}
const ChatScreen = () => {
  const [messages, setMessages] = useState([]);
  const [isOpen, setOpen] = useState(true);
  let params = useParams();
  const caseId = params.caseId;

  // try
  const [suspectedSymptoms, setSSymptoms] = useState([]);
  const [suspectedDiseases, setSDiseases] = useState([]);

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
      "Content-Type": "application/json",
      Accept: "application/json",
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
    setSSymptoms(data.symptoms);
    setSDiseases(data.diseases);
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
    setSSymptoms(data.symptoms);
    setSDiseases(data.diseases);
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
    setSSymptoms(messages[mIndex].symptoms.map((s) => s));
    setMessages(messages.map((m) => m));
  };

  // https://www.chatbot.com/chatbot-templates/
  return (
    <Grid container p={1} justifyContent="space-evenly">
      <Box display="inline-grid" sx={{ width: 0.18 }}>
        <Paper elevation={3}>
          <Grid item>
            <h4>Suspected Symptoms</h4>
            <Symptom
              symptoms={suspectedSymptoms}
              onToggle={toggleConfirm}
              messageIndex={messages.length - 1}
            ></Symptom>
          </Grid>
        </Paper>
      </Box>
      <Box display="block" sx={{ width: 0.6 }}>
        <Paper elevation={3}>
          <Grid item p={2}>
            <Header caseId={caseId} />
            <Topbar />
            <Messages messages={messages} onToggle={toggleConfirm} />
            <Divider />
            <Footer open={isOpen} onSend={sendMessage} />
          </Grid>
        </Paper>
      </Box>
      <Box display="inline-grid" sx={{ width: 0.18 }}>
        <Paper elevation={3}>
          <Grid item>
            <h4>Suspected Diseases</h4>
            <Disease diseases={suspectedDiseases}></Disease>
          </Grid>
        </Paper>
      </Box>
    </Grid>
  );
};

export default ChatScreen;
