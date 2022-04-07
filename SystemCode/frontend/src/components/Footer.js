import { Grid } from "@mui/material";
import { BiSend } from "react-icons/bi";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { useState } from "react";
const Footer = ({ open, onSend }) => {
  const [mBody, setBody] = useState();
  const onClickF = () => {
    console.log("button clicked");
    onSend({ body: mBody, isUser: true });
  };

  const handleChange = (e) => {
    setBody(e.target.value);
  };

  return (
    <Grid mt={3} container direction="row" alignItems="center">
      <Grid item pr={1} xs={10}>
        <TextField
          id="userquery"
          label="User Response"
          multiline
          rows={4}
          fullWidth
          disabled={!open}
          onChange={handleChange}
        />
      </Grid>
      <Grid item xs={2} alignItems="flex-end">
        <Grid container direction="column" alignContent="flex-end">
          <Button variant="contained" onClick={onClickF}>
            <BiSend />
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Footer;
