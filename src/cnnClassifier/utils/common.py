import os 
from box.exceptions import BoxValueError
import yaml 
from src.cnnClassifier import logger 
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib  import Path 
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input 
    
    Raises:
        ValueError: if yaml file is empty
        e : empty file 

    Returns:
        ConfigBox: ConfigBox type 
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) 
            logger.info(f"yaml file : {path_to_yaml} loaded successfully") 
            return ConfigBox(content) 
    
    except BoxValueError:
        raise ValueError("yaml file is empty") 
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    Create a list of directories. 

    Expected Args:
        path_to_directories (list) : list of path of directories 
        ignore_log (bool, optional) : ignore if mulitple directories is needed. 
    '''

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True) 
        if verbose:
            logger.info(f"Created directory at : {path}") 

@ensure_annotations
def save_json(path: Path, data: dict):
    '''
    Save json data. 

    Args: 
        path (Path) : path to the json file 
        data (dict) : data to be saved in the json file .
    '''

    with open(path, "w") as f:
        json.dump(data, f, indent = 4) 
    
    logger.info(f"Json file saved at {path}")

@ensure_annotations
def load_json(path: Path) ->ConfigBox: 
    '''
    Load the json file's data. 

    Arguments: 
        path (Path) : path to the json file 
    
    Returns:
        ConfigBox: data ass class attiributes, instead of dict. 
    '''

    with open(path) as f:
        content = json.load(f) 

    logger.info(f"Json file successfully loaded from : {path}") 
    return ConfigBox(content) 

@ensure_annotations
def save_bin(data: Any, path: Path): 
    '''
    Saving binary files: 

    Args: 
        data (Any) : data to be saved as binary
        path (Path) : path to the binary file
    '''

    joblib.dump(value=data, filename=path) 
    logger.info(f"Binary file saved at : {path}") 

@ensure_annotations
def load_bin(path: Path) -> Any:
    '''Load the binary data: 
        
        Args:
            path (Path) : path to the binary file 

        Returns: 
            Any : object stored in the file gets returned. 
    '''

    data = joblib.load(path) 
    logger.info(f"Binary file loaded from : {path}")
    return data 

@ensure_annotations
def get_size(path: Path) -> str: 
    '''Get size in kBs 
        Args : 
            path (Path) : path to the file 
        Return : 
        str : size in kBs
    '''

    size_in_kb = round(os.path.getsize(path)/1024) 
    return f"~{size_in_kb} KBs"

def decodeImage(imgstring, fileName): 
    imgdata = base64.b64decode(imgstring) 
    with open(fileName, "wb") as f:
        f.write(imgdata) 
        f.close() 

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())