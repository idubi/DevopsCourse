import React, { useState } from "react";
import styled from "styled-components";
function FileBrowser() {
  const [path, setPath] = useState("");
  // const [response, setResponse] = useState("");

  const handlePathChange = (event) => {
    setPath(event.target.value);
  };

  const handleExecute = () => {
    //   fetch(path)
    //     .then((response) => response.json())
    //     .then((data) => setResponse(JSON.stringify(data)))
    //     .catch((error) => console.error("Error:", error));
  };

  return (
    <Container>
      <Upper>
        <h1>Folder selection</h1>
        <input type="text" value="./public/" disabled />
        <input type="text" value={path} onChange={handlePathChange} />
        <button onClick={handleExecute}>Execute</button>
      </Upper>
      <Lower>
        <LeftLowerDiv>files list</LeftLowerDiv>
        <RightLowerDiv>selected file content</RightLowerDiv>
      </Lower>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 90%;
  width: 90%;
`;

const Upper = styled.div`
  height: 30%;
  background-color: lightgrey;
`;

const Lower = styled.div`
  display: flex;
  flex-direction: row;
  height: 100%;
`;

const LeftLowerDiv = styled.div`
  width: 30%;
  height: 100%;
  background-color: gray;
`;
const RightLowerDiv = styled.div`
  width: 70%;
  height: 100%;
  background-color: gray;
`;

export default FileBrowser;
