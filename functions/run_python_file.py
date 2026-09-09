import os
import subprocess
from functions.validators import validate_path
from functions.error import InvalidPathError, FileExecutionError, PathTypeError


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        absolute_file_path = validate_path(working_directory, file_path, "execute")
        
        
        if os.path.isfile(absolute_file_path):
            
            if not absolute_file_path.endswith('.py'):
                raise PathTypeError(f'"{file_path}" is not a Python file')


            command = ["python", absolute_file_path]
            if args:
                command.extend(args)
            result: subprocess.CompletedProcess = subprocess.run(
                    command,
                    cwd=os.path.abspath(working_directory),
                    text=True, 
                    timeout=30, 
                    capture_output=True)
        
            output = []

            if not result.stdout and not result.stderr:
                output.append("No output produced")
            elif result.returncode != 0:
                output.append(f"Process exited with code {result.returncode}")
            
            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")
            
            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")
                        
            return '\n'.join(output)

        
        raise FileExecutionError(f'"{file_path}" does not exist or is not a regular file')


    except (InvalidPathError, PathTypeError, FileExecutionError) as e:
        return f'Error: {str(e)}' 

    except Exception as e:
        return f'Error: executing Python file: {str(e)}'

    

               

    
