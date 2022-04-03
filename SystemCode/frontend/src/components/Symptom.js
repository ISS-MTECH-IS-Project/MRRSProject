import React from "react";
import PropTypes from "prop-types";

// image here should be fully form URL -> Do the heavy work at server side
const Symptom = ({ symptoms }) => {
  return (
    <div>
      {symptoms.map((s, i) => (
        <React.Fragment key={"Sym" + i}>
          <div>Symptom Name: {s.name}</div>
          <div>Symptom Description: {s.confirmed}</div>
          <div>Symptom Image: {s.image}</div>
          <div>Symptom Question: {s.question}</div>
        </React.Fragment>
      ))}
    </div>
  );
};

Symptom.propTypes = { symptoms: PropTypes.array };

export default Symptom;
