import React from "react";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Card from "@mui/material/Card";
import {
  CardActionArea,
  CardActions,
  CardMedia,
  Modal,
  Box,
} from "@mui/material";
import { makeStyles } from "@mui/styles";
import { Grid } from "@mui/material";

// image here should be fully form URL -> Do the heavy work at server side
const Symptom = ({ symptoms, messageIndex, onToggle, isHistory = false }) => {
  const handleClick = (i, e) => {
    console.log("toggle");
    onToggle(messageIndex, i);
  };

  const useStyles = makeStyles({
    cardC: {
      backgroundColor: "#3D426B",
      color: "white",
      boxShadow: "none",
    },
    cardNC: {
      backgroundColor: "white",
      color: "black",
    },
  });

  const modalstyle = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: "80%",
    bgcolor: "background.paper",
    border: "2px solid #000",
    boxShadow: 24,
    p: 4,
  };

  const [currentImg, setImg] = React.useState("");
  const [openModal, setOpenModal] = React.useState(false);
  const handleOpen = (img) => {
    setImg(img);
    setOpenModal(true);
  };
  const handleClose = () => setOpenModal(false);

  const classes = useStyles();

  return (
    <Grid container direction="row" flexWrap="wrap" alignItems="flex-end">
      <Modal open={openModal} onClose={handleClose} width={500}>
        <Box sx={modalstyle}>
          <Card>
            <CardMedia
              component="img"
              image={"/Images/" + currentImg + ".jpg"}
            ></CardMedia>
          </Card>
        </Box>
      </Modal>
      {symptoms.map((s, i) => (
        <Grid item alignItems="flex" key={"Sym" + i}>
          {/* <div>Symptom Name: {s.name}</div> */}
          <Card
            sx={{ m: 2 }}
            className={s.confirmed ? classes.cardC : classes.cardNC}
          >
            {s.image !== "nan" ? (
              <CardMedia
                height={150}
                width={200}
                component="img"
                image={"/static/Images/" + s.image + ".jpg"}
                onClick={() => handleOpen(s.image)}
                title={s.name}
              ></CardMedia>
            ) : (
              <div></div>
            )}
            <CardActions>
              <FormGroup>
                <FormControlLabel
                  control={<Checkbox checked={s.confirmed} />}
                  label={s.question}
                  disabled={isHistory}
                  onChange={(e) => handleClick(i, e)}
                ></FormControlLabel>
              </FormGroup>
            </CardActions>
          </Card>

          {/* <button onClick={(e) => handleClick(i, e)}>
            {s.confirmed ? <BiCheckCircle /> : <BiCircle />}
          </button>
          <div>Symptom Image: {s.image}</div>
          <div>Symptom Question: {s.question}</div> */}
        </Grid>
      ))}
    </Grid>
  );
};

export default Symptom;
