import os
from functions.error import PathTypeError
from functions.validators import validate_path

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        target_file = validate_path(working_directory, file_path, "write")
        if os.path.isdir(target_file):
            raise PathTypeError(f'Cannot write to "{file_path}" as it is a directory')
        
        os.makedirs(file_path, exist_ok=True)

        with open(target_file, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



    except Exception as e:
        return f'Error: {str(e)}'
    
