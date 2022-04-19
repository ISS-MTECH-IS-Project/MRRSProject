import React, { useEffect, useState } from "react";
import Tooltip from "@mui/material/Tooltip";
import ThumbDownOffAltIcon from "@mui/icons-material/ThumbDownOffAlt";
import ThumbUpOffAltIcon from "@mui/icons-material/ThumbUpOffAlt";
import {
  Box,
  Button,
  ButtonGroup,
  Card,
  CardActions,
  CardMedia,
  CardContent,
  Modal,
  Typography,
} from "@mui/material";

const Disease = ({ d, i, caseId }) => {
  const [rating, setRating] = useState(d.rating);
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

  const confirmStyle = {
    bgcolor: "#CEE5ED",
  };

  const alignCenter = {
    alignItems: "center",
  };

  const likeClick = () => {
    if (rating === 1) {
      setRating(0);
    } else {
      setRating(1);
    }
  };
  const dislikeClick = () => {
    if (rating === -1) {
      setRating(0);
    } else {
      setRating(-1);
    }
  };

  useEffect(() => {
    const updateRating = async () => {
      await fetch(`http://localhost:5000/cases/${caseId}/rating`, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({ diseaseName: d.name, rating: rating }),
      });
    };
    updateRating();
  }, [rating, caseId, d.name]);
  const diseaseStyle = {};
  return (
    <>
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
      <React.Fragment>
        <Card sx={parseFloat(d.confidence) >= 70 ? confirmStyle : diseaseStyle}>
          <CardContent>
            <Typography sx={{ fontSize: 14 }} gutterBottom>
              Suspected Disease ({i + 1})
            </Typography>
            <Typography
              sx={{ mb: 2 }}
              color="#3D426B"
              fontWeight="bold"
              variant="h5"
              paddingLeft="10px"
              component="div"
            >
              {d.name}
              {d.aka ? " (" + d.aka + ")" : ""} - confidence ({d.confidence})
            </Typography>
            <Typography
              sx={{ fontSize: 14 }}
              color="text.secondary"
              gutterBottom
            >
              Causes
            </Typography>
            <Typography paddingLeft="10px" variant="body2" sx={{ mb: 2 }}>
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
                    <Typography
                      paddingLeft="10px"
                      variant="body1"
                      sx={{ pr: 2 }}
                    >
                      {dsi + 1}.{ds.description}
                    </Typography>
                    {ds.image !== "nan" && (
                      <Button size="small" onClick={() => handleOpen(ds.image)}>
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
            <Typography paddingLeft="10px" variant="body2">
              {d.treatment}
            </Typography>
            <Typography
              sx={{ fontSize: 14, mt: 2 }}
              color="text.secondary"
              gutterBottom
            >
              Known Medication
            </Typography>
            {d.medication !== undefined && d.medication.length > 0 ? (
              d.medication.map((dm, dmi) => (
                <React.Fragment key={"DisMed" + dmi}>
                  <CardActions>
                    <Typography
                      paddingLeft="10px"
                      variant="body2"
                      sx={{ pr: 2 }}
                    >
                      {dmi + 1}.{dm.description}
                    </Typography>
                    {dm.hasOwnProperty("url") && (
                      <Button size="small" onClick={() => handleKoyo(dm.url)}>
                        {bullet}COMMERCIAL LINK
                      </Button>
                    )}
                  </CardActions>
                </React.Fragment>
              ))
            ) : (
              <Typography paddingLeft="10px" variant="body2" sx={{ pr: 2 }}>
                N/A
              </Typography>
            )}
            {parseFloat(d.confidence) >= 70 && (
              <ButtonGroup orientation="horizontal" sx={alignCenter}>
                Is this helpful?{"    "}
                <Tooltip title="This disease helps me.">
                  <Button
                    onClick={likeClick}
                    variant={rating === 1 ? "contained" : "outline"}
                  >
                    <ThumbUpOffAltIcon />
                  </Button>
                </Tooltip>
                <Tooltip title="This disease does not help me.">
                  <Button
                    onClick={dislikeClick}
                    variant={rating === -1 ? "contained" : "outline"}
                  >
                    <ThumbDownOffAltIcon />
                  </Button>
                </Tooltip>
              </ButtonGroup>
            )}
          </CardContent>
        </Card>
      </React.Fragment>
    </>
  );
};

export default Disease;
