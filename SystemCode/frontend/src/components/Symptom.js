import React from "react";

function Symptom(props) {
  return (
    <>
      <div>Symptom description: {props.description}</div>
      <div>Symptom description: {props.name}</div>
      <div>Symptom description: {props.image}</div>
      <div>Symptom description: {props.confirmed}</div>
    </>
  );
}

Symptom.propTypes = {};

export default Symptom;
