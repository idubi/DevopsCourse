import React, { useState } from 'react';

function FileExplorerPage() {
  const [directoryPath, setDirectoryPath] = useState('');
  const [filePattern, setFilePattern] = useState('');

  const handleDirectoryChange = async () => {
    try {
      const directoryHandle = await window.showDirectoryPicker('documents',{});
      setDirectoryPath(directoryHandle.name);
    } catch (error) {
      console.error('Error selecting directory:', error);
    }
  };

  const handleSubmit = () => {
    const requestData = {
      path: directoryPath,
      file_pattern: filePattern
    };

    fetch('http://127.0.0.1:5000/check-subfolder-files', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestData)
    })
      .then((response) => response.json())
      .then((data) => {
        // Process the response data here
        console.log(data);
      })
      .catch((error) => {
        // Handle any error that occurred during the request
        console.error(error);
      });
  };

  return (
    <div>
      <button onClick={handleDirectoryChange}>Select Directory</button>
      <input
        type="text"
        value={directoryPath}
        disabled
      />
      <input
        type="text"
        value={filePattern}
        onChange={(event) => setFilePattern(event.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default FileExplorerPage;
