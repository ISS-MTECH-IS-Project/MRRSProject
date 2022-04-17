import { ButtonGroup, Grid } from "@mui/material";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { useState } from "react";
import Tooltip from "@mui/material/Tooltip";
import RestartAltIcon from "@mui/icons-material/RestartAlt";
import CheckBoxOutlineBlankIcon from "@mui/icons-material/CheckBoxOutlineBlank";
import CheckBoxIcon from "@mui/icons-material/CheckBox";
import SendIcon from "@mui/icons-material/Send";

const Footer = ({ open, onSend, toggleOpen }) => {
  const [mBody, setBody] = useState();
  const [chatDisable, setChatDisable] = useState(true);
  const [firstTime, setFirstTime] = useState(true);
  const onClickF = () => {
    console.log("button clicked");
    const message = mBody;
    onSend({ body: message, isUser: true });
    setBody("");
    setFirstTime(false);
  };

  const toggleChat = () => {
    setChatDisable(!chatDisable);
  };

  const onClickRestart = () => {
    window.open("/");
  };

  const handleChange = (e) => {
    setBody(e.target.value);
  };

  return (
    <Grid mt={3} container direction="row" alignItems="center">
      <Grid item pr={1} xs={10}>
        <TextField
          id="userquery"
          label="Describe your pet fish's symptoms"
          multiline
          rows={4}
          fullWidth
          disabled={!firstTime && chatDisable}
          onChange={handleChange}
          value={mBody}
          placeholder="My pet fish is suffering from..."
        />
      </Grid>
      <Grid item xs={2} alignItems="flex-end">
        <Grid container direction="column" alignContent="flex-end">
          <ButtonGroup orientation="vertical">
            <Tooltip title="Send my response">
              <Button
                variant="contained"
                sx={{ mb: 4, mt: 6 }}
                onClick={onClickF}
                endIcon={<SendIcon />}
              >
                Send
              </Button>
            </Tooltip>
            <Tooltip title="Enable the chat box. You cannot disable when the page loads.">
              <Button
                variant="contained"
                sx={{ mb: 4 }}
                onClick={toggleChat}
                endIcon={
                  !firstTime && chatDisable ? (
                    <CheckBoxOutlineBlankIcon />
                  ) : (
                    <CheckBoxIcon />
                  )
                }
              >
                Enable Chat
              </Button>
            </Tooltip>
            <Tooltip title="Allow the bot to return suspected symptoms.">
              <Button
                variant="contained"
                sx={{ mb: 4 }}
                onClick={toggleOpen}
                endIcon={open ? <CheckBoxOutlineBlankIcon /> : <CheckBoxIcon />}
              >
                Enable Guide
              </Button>
            </Tooltip>
            <Tooltip title="Start a new diagnosis">
              <Button
                variant="contained"
                color="error"
                sx={{ mb: 4 }}
                onClick={onClickRestart}
                endIcon={<RestartAltIcon />}
              >
                Restart
              </Button>
            </Tooltip>
          </ButtonGroup>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Footer;
