import { useState, useEffect, useRef } from "react";
import { useParams } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import Topbar from "./Topbar";
import Messages from "./Messages";
import Symptom from "./Symptom";
import Diseases from "./Diseases";
import { Box, Grid } from "@mui/material";
import Paper from "@mui/material/Paper";
import Divider from "@mui/material/Divider";
import moment from "moment";
import { makeStyles } from "@mui/styles";

// message : {isSend, isUser, nextOpen, symptoms, diseases, time, body}
const ChatScreen = () => {
  const [messages, setMessages] = useState([]);
  const [isOpen, setOpen] = useState(false);
  let params = useParams();
  const caseId = params.caseId;

  // try
  const [suspectedSymptoms, setSSymptoms] = useState([]);
  const [suspectedDiseases, setSDiseases] = useState([]);

  const useStyles = makeStyles({
    root: {
      position: "fixed",
      top: "5px",
      width: "35vw",
      right: "2vw",
      overflowY: "scroll",
      maxHeight: "100vh",
    },

    sstitle: {
      backgroundColor: "#3D426B",
      color: "white",
      marginBottom: "0",
      paddingLeft: "10px",
      height: "5vh",
      display: "flex",
      alignItems: "center",
    },
  });

  useEffect(() => {
    const getMessages = async () => {
      const caseDetail = await fetchCase(caseId);
      setMessages(caseDetail.messages);
    };

    getMessages();
  }, [caseId]);

  useEffect(() => {
    const updateMessages = async (id) => {
      await fetch(`http://localhost:5000/cases/${id}`, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(messages),
      });
    };
    if (messages.length > 0) {
      updateMessages(caseId);
    }
  }, [messages, caseId]);

  // Fetch case
  const fetchCase = async (id) => {
    const res = await fetch(`http://localhost:5000/cases/${id}`, {
      headers: {
        "Content-type": "application/json",
      },
    });
    const data = await res.json();
    return data;
  };

  // get next message
  const getNext = async (message) => {
    var mIndex = messages.length - 1;
    for (var i = messages.length - 1; i > 0; i--) {
      if (
        messages[i].symptoms !== undefined &&
        messages[i].symptoms.length > 0
      ) {
        mIndex = i;
        break;
      }
    }
    const m = messages[mIndex];
    const tempBody = m.body;
    m.body = message.body;
    const uri = isOpen ? "open" : "guided";
    const res = await fetch(`http://localhost:5000/cases/${caseId}/${uri}`, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(m),
    });
    const data = await res.json();
    m.body = tempBody;
    data.time = moment().format("hh:mm");
    setMessages([...messages, message, data]);
    setSSymptoms(data.symptoms);
    setSDiseases(data.diseases);
    scrollToBottom();
  };

  const resetDisease = async (s) => {
    const m = {};
    m.symptoms = [s];
    const res = await fetch(`http://localhost:5000/cases/${caseId}/guided`, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(m),
    });
    const data = await res.json();
    setSDiseases(data.diseases);
  };

  const sendMessage = (message) => {
    message.time = moment().format("hh:mm");
    setMessages([...messages, message]);
    getNext(message);
  };

  // Toggle Reminder
  const toggleConfirm = (mIndex, sIndex) => {
    messages[mIndex].symptoms[sIndex].confirmed =
      !messages[mIndex].symptoms[sIndex].confirmed;
    setSSymptoms(messages[mIndex].symptoms.map((s) => s));
    setMessages(messages.map((m) => m));
    resetDisease(messages[mIndex].symptoms[sIndex]);
  };

  const toggleOpen = () => {
    setOpen(!isOpen);
  };

  const messagesEndRef = useRef(null);
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const classes = useStyles();

  // https://www.chatbot.com/chatbot-templates/
  return (
    <Grid container p={1} justifyContent="left">
      <Box display="none" sx={{ width: 0.18 }}>
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
      <Box display="inline-grid" sx={{ width: 0.6 }}>
        <Paper elevation={3}>
          <Grid item p={2}>
            <Header caseId={caseId} />
            <Topbar />
            <Messages messages={messages} onToggle={toggleConfirm} />
            <Divider sx={{ mt: 2 }} />
            <Footer
              open={isOpen}
              onSend={sendMessage}
              toggleOpen={toggleOpen}
            />
            <div ref={messagesEndRef} />
          </Grid>
        </Paper>
      </Box>
      {suspectedDiseases !== undefined && suspectedDiseases.length > 0 && (
        <Box className={classes.root} display="inline-grid">
          <Paper className={classes.root} elevation={3}>
            <h4 className={classes.sstitle}>Suspected Diseases</h4>
            <Diseases diseases={suspectedDiseases} caseId={caseId}></Diseases>
          </Paper>
        </Box>
      )}
    </Grid>
  );
};

export default ChatScreen;
