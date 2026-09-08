import os
from functions.validators import validate_path
from functions.error import PathError, PathTypeError


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        target_execute = validate_path(working_directory, file_path, "execute")
        
        if os.path.isfile(target_execute):
            
            if not target_execute[-4:] == ".py":
                raise PathTypeError(f'"{file_path}" is not a Python file')

            command = ["python", target_execute]
            command.extend(args)

            

    

        raise PathError(f'"{file_path}" does not exist or is not a regular file')
       

    except Exception as e:
        return f'Error: {str(e)}' 

