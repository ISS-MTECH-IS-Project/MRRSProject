import Message from "./Message";
import React, { useEffect, useRef } from "react";

const Messages = ({ messages, onToggle }) => {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="lc-massage-box">
      <div className="lc-massage-seperator" />
      <div
        className="lc-massage-grid"
        role="grid"
        aria-live="polite"
        aria-relevant="additions"
        tabIndex="-1"
      >
        {messages.map((m, i) => (
          <Message
            key={"ID" + i}
            messageIndex={i}
            message={m}
            onToggle={onToggle}
          />
        ))}
        <div ref={messagesEndRef} />
      </div>
    </div>
  );
};

export default Messages;
