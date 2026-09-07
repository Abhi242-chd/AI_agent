import os
from functions.error import InvalidPathError

def validate_path(working_directory: str, path: str, mode: str = "read") -> str: 
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_dir, path))
    is_within_working_dir = os.path.commonpath([abs_working_dir, target_path]) == abs_working_dir

    if not is_within_working_dir:
        raise InvalidPathError(f'Cannot {mode} "{path}" as it is outside the permitted working directory')
    return target_path

