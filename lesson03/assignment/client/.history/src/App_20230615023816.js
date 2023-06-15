import "./App.css";
import "./components/FilesBrowser";
import FileBrowser from "./components/FilesBrowser";
import styled from "styled-components";

function App() {
  return (
    <Container className="App">
      <header className="App-header">
        <FileBrowser></FileBrowser>
      </header>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 1000%;
`;

export default App;
