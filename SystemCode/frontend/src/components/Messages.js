import Message from "./Message";
import React, { useEffect, useRef } from "react";
import Grid from "@mui/material/Grid";

const Messages = ({ messages, onToggle }) => {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <Grid>
      {messages.map((m, i) => (
        <Message
          key={"ID" + i}
          messageIndex={i}
          message={m}
          onToggle={onToggle}
        />
      ))}
      <div ref={messagesEndRef} />
    </Grid>
  );
};

export default Messages;
