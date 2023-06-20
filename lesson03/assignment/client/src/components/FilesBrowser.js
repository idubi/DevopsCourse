import React, { useState,useEffect} from "react"
import { FilesApi } from "../apis/FilesApi.js"
import styled from "styled-components";
import FilesList from "./FilesList.js";
import FileContext from "./FileContext.js";

const INITIAL_PATH = './public/'
const BROWSE_ROOT = './server/public/'

let path = BROWSE_ROOT
let partialPath = '';

const FileBrowser = () => {

  const [filesData,setFilesData]=useState()
  const [selectedFileDataContent, setSelectedFileDataContent] = useState('');
  const [visibleUpButton, setVisibleUpButton] = useState(false);
  
  useEffect(() => {
    loadPathFiles()
     
}, []);

   
  const setPath = () => {
    path = BROWSE_ROOT + partialPath
   
    if (partialPath) 
       setVisibleUpButton(true)
    else 
       setVisibleUpButton(false)
    console.log('path =', path);
  }

  const setPartialPath = (path) => {
    if (path) {
      const lastChar = path.charAt(path.length - 1)
      if (lastChar !== "/" )
      { 
        path = path + '/'       
      }
    }
      partialPath = path
   

  }
 

  const loadPathFiles = async () => {
    FilesApi.listFilesAndFolders(path).then((items) => {
            console.log('listFilesAndFolders : ' , items);
            setFilesData(items && items.files)
          }).catch(err =>{
            console.log(err);
          })
  }

  const handlePathChange = (event) => {
    setPath();
  };

  const loadFileData =  async (filePath) => {
    console.log('loadFileData , filePath=',filePath );
    try{
      const data = await FilesApi.loadFileContent(filePath)
      return (data.content )
    }
    catch (error) {
      console.log(error);
    }
    
    
  }

  const handleSelectedFile = async (file) => {
   
    const selectedFileName = file.target.textContent
    console.log(selectedFileName);
    const fileData = await  loadFileData(`${path}${selectedFileName}`)
    if (fileData){
      setSelectedFileDataContent(fileData);
    } else {
      setPartialPath((partialPath||'')+selectedFileName+'/')
      setPath()
      loadPathFiles()
    }
  };

  const goBackDirectory = () => {
      let url = ''
      if (partialPath) 
        url = partialPath.split('/').slice(0, -2).join('/')
        setPartialPath(url)
        setPath()
        loadPathFiles()
       
      

        
  }
   
 
  return (
   
    <Container>
      <Upper>
        <h1>Folder selection</h1>
        {visibleUpButton  && 
            <buton  onClick={goBackDirectory} >
                <img  src="upArrow.png" height="15px" alt=""/>
            </buton> }
        
        
        <Label type="text" value={INITIAL_PATH} disabled />
        <Path id='_path'   onChange={handlePathChange} value={partialPath} readOnly/>
        {/* <button id='_setPath' onClick={loadPathFiles}>load files in path</button> */}
      </Upper>
      <Lower>
        
        <LeftLowerDiv><FilesList data={filesData} onSelecFile={handleSelectedFile}/> </LeftLowerDiv>
        <RightLowerDiv><FileContext data={selectedFileDataContent}/></RightLowerDiv>
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
  background-color: lightgrey;
  300px;
`;

const Lower = styled.div`
  display: flex;
  flex-direction: row;
  height : 700px;  
  color: #abc3a7;
`;

const LeftLowerDiv = styled.div`
  width: 35%;
  height: 100%;
  background-color: gray;
`;
const RightLowerDiv = styled.div`
  width: 65%;
  height: 100%;
  background-color: #ffffff; 
`;


const Path = styled.input`
  background-color: white;
  width: 350;
`;

const Label = styled.input`
  background-color: lightgrey;
  width: 60px;
`;

 


export default FileBrowser;
