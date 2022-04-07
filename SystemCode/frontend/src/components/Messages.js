import Message from "./Message";
import Grid from "@mui/material/Grid";

const Messages = ({ messages, onToggle }) => {
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
    </Grid>
  );
};

export default Messages;
