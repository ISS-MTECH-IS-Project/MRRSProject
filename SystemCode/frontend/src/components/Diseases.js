import React from "react";
import PropTypes from "prop-types";
import Disease from "./Disease";

const Diseases = ({ diseases, caseId }) => {
  return (
    <div>
      {diseases !== undefined &&
        diseases.length > 0 &&
        diseases.map((d, i) => (
          <Disease key={"Dis" + i} d={d} i={i} caseId={caseId} />
        ))}
    </div>
  );
};

Diseases.propTypes = { diseases: PropTypes.array };

export default Diseases;
