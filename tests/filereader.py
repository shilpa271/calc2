"""Read CSV"""
import pandas as pd
from tests.filewriter import Filewriter
#pylint: disable=import-error

# pylint: disable=trailing-newlines,missing-class-docstring,missing-function-docstring,no-self-argument,too-few-public-methods
class FileReader():
    def readcsv(filepath):
        file = pd.read_csv(filepath)
        return Filewriter(file)
