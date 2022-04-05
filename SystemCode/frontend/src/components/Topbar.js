import SmartToyIcon from "@mui/icons-material/SmartToy";
import { Box } from "@mui/material";
import Grid from "@mui/material/Grid";

const Topbar = () => {
  return (
    <div id="title" className="titlebar">
      <Grid container direction="row" alignItems="center">
        <SmartToyIcon />
        <Box m={2} pt={3}></Box>
        OhMyFishBot is here to serve
      </Grid>
    </div>
  );
};
export default Topbar;
