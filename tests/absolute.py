# pylint: disable=missing-module-docstring
from pathlib import Path
# pylint: disable=missing-module-docstring,missing-final-newline
def path(filepath):
    """relative path calls it and then returns the absolute path"""
    relativepath = Path(filepath)
    return relativepath.absolute()