import Message from "./Message";

const Messages = ({ messages, onToggle }) => {
  return (
    <div class="lc-massage-box">
      <div class="lc-massage-seperator" />
      <div
        class="lc-massage-grid"
        role="grid"
        aria-live="polite"
        aria-relevant="additions"
        tabIndex="-1"
      >
        {messages.map((m, i) => (
          <Message messageIndex={i} message={m} onToggle={onToggle} />
        ))}
      </div>
    </div>
  );
};

export default Messages;
