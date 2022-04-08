import { Navigate } from "react-router-dom";
import { useState, useEffect } from "react";
function CreateCase() {
  const [caseId, setCaseId] = useState();
  useEffect(() => {
    const createNewCase = async () => {
      const caseDetail = await createCase();
      setCaseId(caseDetail.name);
    };
    createNewCase();
  }, []);
  const createCase = async () => {
    const res = await fetch(`http://localhost:5000/cases`, {
      method: "POST",
    });
    const data = await res.json();
    return data;
  };
  return <>{caseId ? <Navigate to={"/chat/" + caseId} /> : <div></div>}</>;
}

export default CreateCase;
