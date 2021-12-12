
import pandas as pd

from tests.absolute import absolutepath

file_name = "tests/data/output.csv"


class Read:
    @staticmethod
    def DataFrameFromCSVFile():
        file = pd.read_csv(absolutepath(file_name))
        return file


