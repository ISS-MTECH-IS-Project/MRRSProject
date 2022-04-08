import { Grid } from "@mui/material";
import { BiSend } from "react-icons/bi";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";

const Footer = ({ open, onSend }) => {
  const onClickF = () => {
    console.log("button clicked");
    onSend({});
  };
  return (
    <Grid mt={2} container direction="row" alignItems="center">
      <Grid item pr={1} xs={10}>
        <TextField
          id="userquery"
          label="User Response"
          multiline
          rows={4}
          defaultValue="How is your fish?"
          fullWidth
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
