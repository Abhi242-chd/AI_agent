import os
from os.path import isfile
from config import MAX_CHARS
from functions.get_files_info import Error

def get_file_content(working_directory: str, file_path: str) -> str: 
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        is_within_working_dir = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not is_within_working_dir:
            raise Error(f'Cannot read "{file_path}" as it is outside the permitted working directory')
            
        elif os.path.isfile(target_file):

            with open(target_file, "r") as f:
                content = f.read(MAX_CHARS)
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
                return content
        
        raise Error(f'File not found or is not a regular file: "{file_path}"')

            
    except Exception as e:
        return f'Error: {str(e)}'

    
    
        

