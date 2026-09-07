import os
from functions.error import PathTypeError
from functions.validators import validate_path

def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    def format_directory_listing(entries: list) -> str:
        def line_format(filename: str) -> str:
            filepath = os.path.join(target_dir, filename)
            return f' - {filename}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}'
        
        return "\n".join(map(line_format, entries))
        

    try:
        target_dir = validate_path(working_directory, directory)
        if not os.path.isdir(target_dir):
            raise PathTypeError(f'"{directory}" is not a directory')
        elif os.path.isdir(target_dir):
            return format_directory_listing(os.listdir(target_dir))
    except Exception as e:
        return f'Error: {str(e)}'
    
