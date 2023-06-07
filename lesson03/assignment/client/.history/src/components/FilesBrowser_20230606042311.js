import React, { useState } from 'react';

function App() {
  const [path, setPath] = useState('');
  const [response, setResponse] = useState('');

  const handlePathChange = (event) => {
    setPath(event.target.value);
  };

  const handleExecute = () => {
    fetch(path)
      .then((response) => response.json())
      .then((data) => setResponse(JSON.stringify(data)))
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div>
      <h1>REST Call App</h1>
      <input type="text" value={path} onChange={handlePathChange} />
      <button onClick={handleExecute}>Execute</button>
      <pre>{response}</pre>
    </div>
  );
}

export default App;

