import React from "react";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Card from "@mui/material/Card";
import { CardActionArea, CardActions, CardMedia } from "@mui/material";

// image here should be fully form URL -> Do the heavy work at server side
const Symptom = ({ symptoms, messageIndex, onToggle }) => {
  const handleClick = (i, e) => {
    console.log("toggle");
    onToggle(messageIndex, i);
  };

  return (
    <div>
      {symptoms.map((s, i) => (
        <React.Fragment key={"Sym" + i}>
          {/* <div>Symptom Name: {s.name}</div> */}
          <Card>
            <CardMedia
              height={200}
              component="img"
              image={require("../Images/bloat.jpg")} // require image
              title={s.name}
            ></CardMedia>
            <CardActions>
              <FormGroup>
                <FormControlLabel
                  control={<Checkbox checked={s.confirmed} />}
                  label={s.question}
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
        </React.Fragment>
      ))}
    </div>
  );
};

export default Symptom;
