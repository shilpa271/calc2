# pylint: disable=missing-module-docstring
from pathlib import Path
# pylint: disable=missing-module-docstring
def path(filepath):
    """relativepath calls the path object and then returns the absolute path"""
    relativepath = Path(filepath)
    return relativepath.absolute()
