import React from "react";
import PropTypes from "prop-types";

const Disease = ({ diseases }) => {
  return (
    <div>
      {diseases !== undefined &&
        diseases.length > 0 &&
        diseases.map((d, i) => (
          <React.Fragment key={"Dis" + i}>
            <div>Disease Name: {d.name}</div>
            <div>Disease Description: {d.description}</div>
          </React.Fragment>
        ))}
    </div>
  );
};

Disease.propTypes = { diseases: PropTypes.array };

export default Disease;
