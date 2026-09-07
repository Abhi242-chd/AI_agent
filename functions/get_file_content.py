import os
from os.path import isfile
from config import MAX_CHARS
from functions.error import PathError
from functions.validators import validate_path

def get_file_content(working_directory: str, file_path: str) -> str: 
    try:
        target_file = validate_path(working_directory, file_path)   
        if os.path.isfile(target_file):

            with open(target_file, "r") as f:
                content = f.read(MAX_CHARS)
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
                return content
        
        raise PathError(f'File not found or is not a regular file: "{file_path}"')

            
    except Exception as e:
        return f'Error: {str(e)}'

    
    
        

