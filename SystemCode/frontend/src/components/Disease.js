import React from "react";
import PropTypes from "prop-types";
import {
  Box,
  Button,
  Card,
  CardActionArea,
  CardActions,
  CardMedia,
  CardContent,
  Modal,
  Typography,
} from "@mui/material";
import { setSelectionRange } from "@testing-library/user-event/dist/utils";

const Disease = ({ diseases }) => {
  const [currentImg, setImg] = React.useState("");
  const [openModal, setOpenModal] = React.useState(false);
  const handleOpen = (img) => {
    setImg(img);
    setOpenModal(true);
  };
  const handleClose = () => setOpenModal(false);

  const bullet = (
    <Box
      component="span"
      sx={{ display: "inline-block", mx: "2px", transform: "scale(2)" }}
    >
      •
    </Box>
  );

  const handleKoyo = (url) => {
    window.location = url;
    window.open(url);
  };

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

  return (
    <div>
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
      {diseases !== undefined &&
        diseases.length > 0 &&
        diseases.map((d, i) => (
          <React.Fragment key={"Dis" + i}>
            <Card sx={{ minWidth: 500 }}>
              <CardContent>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  Suspected Disease ({i + 1})
                </Typography>
                <Typography sx={{ mb: 2 }} variant="h5" component="div">
                  {d.name} ({d.aka})
                </Typography>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  Causes
                </Typography>
                <Typography variant="body2" sx={{ mb: 2 }}>
                  {d.cause}
                </Typography>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  Symptoms
                </Typography>
                {d.symptoms !== undefined &&
                  d.symptoms.length > 0 &&
                  d.symptoms.map((ds, dsi) => (
                    <React.Fragment key={"DisSym" + dsi}>
                      <CardActions>
                        <Typography variant="body1" sx={{ pr: 2 }}>
                          {dsi + 1}.{ds.description}
                        </Typography>
                        {ds.image !== "nan" && (
                          <Button
                            size="small"
                            onClick={() => handleOpen(ds.image)}
                          >
                            {bullet}See Photo
                          </Button>
                        )}
                      </CardActions>
                    </React.Fragment>
                  ))}

                <Typography
                  sx={{ fontSize: 14, mt: 2 }}
                  color="text.secondary"
                  gutterBottom
                >
                  Treatment
                </Typography>
                <Typography variant="body2">{d.treatment}</Typography>
                <Typography
                  sx={{ fontSize: 14, mt: 2 }}
                  color="text.secondary"
                  gutterBottom
                >
                  Known Medication
                </Typography>
                {d.medication !== undefined &&
                  d.medication.length > 0 &&
                  d.medication.map((dm, dmi) => (
                    <React.Fragment key={"DisMed" + dmi}>
                      <CardActions>
                        <Typography variant="body2" sx={{ pr: 2 }}>
                          {dmi + 1}.{dm.description}
                        </Typography>
                        {dm.hasOwnProperty("url") && (
                          <Button
                            size="small"
                            onClick={() => handleKoyo(dm.url)}
                          >
                            {bullet}COMMERCIAL LINK
                          </Button>
                        )}
                      </CardActions>
                    </React.Fragment>
                  ))}
              </CardContent>
            </Card>
            {/* <div>Disease Vet Advice: {d.vet_advised}</div>
            <div>Disease Cause: {d.environment}</div>
            <div>Disease Cause: {d.affectfish}</div> */}
          </React.Fragment>
        ))}
    </div>
  );
};

Disease.propTypes = { diseases: PropTypes.array };

export default Disease;
