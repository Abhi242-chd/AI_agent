class PathError(Exception):
    pass

class FileExecutionError(Exception):
    pass

class InvalidPathError(PathError):
    pass

class PathTypeError(PathError):
    pass
