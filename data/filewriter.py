"""Write CSV"""

class Write:
    @staticmethod
    def DataFrameToCSVFile(filename_df):
        return filename_df.to_csv('tests/data/addition.csv', mode ='a', index=False, header=False)