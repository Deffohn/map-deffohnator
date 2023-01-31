import os
from os import path


def scan_create_directory_location(
    relative_location: str,
) -> bool:
    is_dir: bool = path.isdir(relative_location)
    if not is_dir:
        try:
            os.makedirs(path.abspath(relative_location), exist_ok=True)
        except:
            return False
    return True
