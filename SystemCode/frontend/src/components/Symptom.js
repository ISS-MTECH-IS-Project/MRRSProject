import React from "react";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Card from "@mui/material/Card";
import { CardContent, CardActions, CardMedia, Modal, Box } from "@mui/material";
import { makeStyles } from "@mui/styles";
import { Grid } from "@mui/material";

import Tooltip from "@mui/material/Tooltip";

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
      width: 300,
      height: 350,
    },
    cardNC: {
      backgroundColor: "white",
      color: "black",
      width: 300,
      height: 350,
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
              image={"/static/Images/" + currentImg}
            ></CardMedia>
          </Card>
        </Box>
      </Modal>
      <Card sx={{ ml: 2, mr: "15vw", fontWeight: "bold" }}>
        <CardContent>
          Please check the boxes if the symptom description applies to your pet
          fish
        </CardContent>
      </Card>
      {symptoms.map((s, i) => (
        <Grid item alignItems="flex" key={"Sym" + i}>
          {/* <div>Symptom Name: {s.name}</div> */}
          <Card
            sx={{ m: 2 }}
            className={s.confirmed ? classes.cardC : classes.cardNC}
          >
            {s.AIconfirmed && (
              <CardContent height={150} width={100}>
                Auto-checked via AI confidence. Please uncheck if inot
                applicable.
              </CardContent>
            )}
            {s.image !== "nan" ? (
              <CardMedia
                height={150}
                width={150}
                component="img"
                image={"/static/Images/" + s.image}
                onClick={() => handleOpen(s.image)}
                title={s.name}
              ></CardMedia>
            ) : (
              <div></div>
            )}
            <Tooltip title="Check if symptom is applicable, otherwise leave it unchecked">
              <CardActions height={100} width={150}>
                <FormGroup>
                  <FormControlLabel
                    control={<Checkbox checked={s.confirmed} />}
                    label={s.question}
                    onChange={(e) => handleClick(i, e)}
                  ></FormControlLabel>
                </FormGroup>
              </CardActions>
            </Tooltip>
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
