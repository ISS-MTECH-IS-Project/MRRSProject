import React from "react";
import { BiCheckCircle, BiCircle } from "react-icons/bi";
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
          <div>Symptom Name: {s.name}</div>
          <button onClick={(e) => handleClick(i, e)}>
            {s.confirmed ? <BiCheckCircle /> : <BiCircle />}
          </button>
          <div>Symptom Image: {s.image}</div>
          <div>Symptom Question: {s.question}</div>
        </React.Fragment>
      ))}
    </div>
  );
};

export default Symptom;
