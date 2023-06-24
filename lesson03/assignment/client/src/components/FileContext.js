import styled from "styled-components";


const FileContext = (fileData) => {
    const data = fileData?.data || ''
    return (   <Textarea  value={data}  readOnly  /> 
    )
    

}

const Textarea= styled.textarea`
    width :99%;
    height:90%;
    border: none;
    outline: none;
    resize: none;      
    overflow: auto;  
    overflow-y: scroll;
     
`

export default FileContext