import "./App.css";
import "./components/FilesBrowser";
import FileBrowser from "./components/FilesBrowser";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <FileBrowser></FileBrowser>
      </header>
    </div>
  );
}

export default App;
