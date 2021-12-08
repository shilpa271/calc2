"""Write CSV"""
import pandas as pd
from calc.calculations.addition import Addition
# pylint: disable=missing-class-docstring,trailing-newlines,trailing-comma-tuple,import-error,missing-function-docstring,invalid-name,unused-variable
def Filewriter(df_from_read):
    df = pd.DataFrame(columns=['value_1', 'value_2', 'result'])
    for index, row in df_from_read.iterows():
        mynumbers = (row['value_1' : row['value_2']]),
        addition = Addition(mynumbers)
        df = df.append({'value_1': row['value1'],
                        'value_2': row['value_2'],'result': addition.get_result()},
                       ignore_index=True)
        df.to_csv('addition.csv', mode='a', index=False, header=False)
        print(df)
