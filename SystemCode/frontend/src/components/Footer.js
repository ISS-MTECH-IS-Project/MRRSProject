import { ButtonGroup, Grid } from "@mui/material";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { useState } from "react";
import Tooltip from "@mui/material/Tooltip";
import RestartAltIcon from "@mui/icons-material/RestartAlt";

import SendIcon from "@mui/icons-material/Send";

const Footer = ({ open, onSend }) => {
  const [mBody, setBody] = useState();
  const onClickF = () => {
    console.log("button clicked");
    const message = mBody;
    onSend({ body: message, isUser: true });
    setBody("");
  };

  const onClickRestart = () => {
    console.log("Restart button clicked");
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
          disabled={!open}
          onChange={handleChange}
          placeholder="My pet fish is suffering from..."
        />
      </Grid>
      <Grid item xs={2} alignItems="flex-end">
        <Grid container direction="column" alignContent="flex-end">
          <ButtonGroup orientation="vertical">
            <Tooltip title="Restart the diagnosis">
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
            <Tooltip title="Send my response">
              <Button
                variant="contained"
                onClick={onClickF}
                endIcon={<SendIcon />}
              >
                Send
              </Button>
            </Tooltip>
          </ButtonGroup>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Footer;
