from functions.edit_file_content import schema_write_file, write_file
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.get_file_content import schema_get_file_content, get_file_content

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]
