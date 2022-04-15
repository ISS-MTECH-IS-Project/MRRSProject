import { BiBot, BiUser } from "react-icons/bi";
import Symptom from "./Symptom";
import { Box, Card, CardContent, Grid } from "@mui/material";
import Paper from "@mui/material/Paper";

const Message = ({ messageIndex, message, onToggle }) => {
  return (
    <>
      {message.isUser ? (
        <Grid container mb={3} direction="column" alignContent="flex-end">
          <Grid item>
            <BiUser />
            <span> Visitor</span>
            <span> @ {message.time}</span>
          </Grid>
          <Grid item display="inline-flex">
            <Paper elevation={1}>
              <Box m={1}>
                <span>{message.body}</span>
              </Box>
            </Paper>
          </Grid>
        </Grid>
      ) : (
        <Grid container direction="column" alignContent="flex-start">
          <Grid item alignItems="flex">
            <BiBot />
            <span> ChatBot</span>
            <span> @ {message.time}</span>
            {message.hasOwnProperty("symptoms") &&
              message.symptoms.length === 0 && (
                <Card>
                  <CardContent>
                    Dear user, I apologise for not understanding your response.
                    <br />
                    Please try to describe your pet fish's symptoms more.
                  </CardContent>
                </Card>
              )}
          </Grid>
          <Grid item display="inline-flex">
            <Paper elevation={1}>
              <Box m={1}>
                <span>{message.body}</span>

                {/* Empty symptoms if display of symptoms is undesired */}
                {message.hasOwnProperty("symptoms") &&
                  message.symptoms.length > 0 && (
                    <Symptom
                      symptoms={message.symptoms}
                      messageIndex={messageIndex}
                      onToggle={onToggle}
                      isHistory={message.isHistory}
                    ></Symptom>
                  )}
              </Box>
            </Paper>
          </Grid>
        </Grid>
      )}
    </>
  );
};

export default Message;
