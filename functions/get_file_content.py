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


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read file contents relative to the working directory, providing the content of the file",
        "parameters": {
            "type": "object",
            "properties": {
                "File path": {
                    "type": "string",
                    "description": "File path to read file contents from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}   
    
        

