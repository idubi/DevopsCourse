import "./App.css";
import "./components/FilesBrowser";
import FileBrowser from "./components/FilesBrowser";
import styled from "styled-components";

function App() {
  return (
    <Container className="App">
      <FileBrowser></FileBrowser>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
`;

export default App;
