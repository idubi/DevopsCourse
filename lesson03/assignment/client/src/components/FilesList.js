const FilesList = ({ data,onSelecFile }) => {
    // Render the tree view based on the data received
    return (
      <ul>
        {data && data.map(item => (
          <li key={item} onClick={onSelecFile}>{item}</li>
        ))}
      </ul>
    );
  };
  export default FilesList;