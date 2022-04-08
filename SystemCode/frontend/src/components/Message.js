import { BiBot, BiUser } from "react-icons/bi";
import Symptom from "./Symptom";
import { Box, Grid } from "@mui/material";
import Paper from "@mui/material/Paper";

const Message = ({ messageIndex, message, onToggle }) => {
  return (
    <>
      <Grid container direction="column" alignItems="flex">
        <Grid item alignItems="flex">
          <BiBot />
          <span> ChatBot</span>
          <span> @ 21:25</span>
        </Grid>
        <Grid item display="inline-flex">
          <Paper elevation={1}>
            <Box m={1}>
              <span>Want to see what I can do?</span>
              {/* Empty symptoms if display of symptoms is undesired */}
              {message.hasOwnProperty("symptoms") && (
                <Symptom
                  symptoms={message.symptoms}
                  messageIndex={messageIndex}
                  onToggle={onToggle}
                ></Symptom>
              )}
            </Box>
          </Paper>
        </Grid>
      </Grid>

      {/* user */}
      <Grid container mb={3} direction="column" alignContent="flex-end">
        <Grid item>
          <BiUser />
          <span> Visitor</span>
          <span> @ 21:26</span>
        </Grid>
        <Grid item display="inline-flex">
          <Paper elevation={1}>
            <Box m={1}>
              <span>hi</span>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </>
  );
};

export default Message;
