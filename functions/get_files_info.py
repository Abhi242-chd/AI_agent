import os
class Error(Exception):
    pass


def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
    is_within_working_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
   

    def format_directory_listing(entries: list) -> str:
        def line_format(filename: str) -> str:
            filepath = os.path.join(target_dir, filename)
            return f' - {filename}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}'
        
        return "\n".join(map(line_format, entries))
        

    try:
        if not is_within_working_dir:
            raise Error(f'Cannot list "{directory}" as it is outside the permitted working directory')
        elif not os.path.isdir(target_dir):
            raise Error('"{directory}" is not a directory')
        elif os.path.isdir(target_dir):
            return format_directory_listing(os.listdir(target_dir))
    except Error as e:
        return f'Error: {str(e)}'
    
