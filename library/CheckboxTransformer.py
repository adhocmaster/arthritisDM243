import pandas as pd
import numpy as np


class CheckboxTransformer:


    def transformByIndex(self, df:pd.DataFrame, startIndex, endIndex):

        for i in range(startIndex, endIndex + 1):

            print(f'transforming column {i}: {df.columns[i]}')

            numberOfVals = len(df.iloc[:, i].value_counts())
            if numberOfVals < 1:
                print(f'column {i}: {df.columns[i]} has no value. filling with zeros')
                df.iloc[:, i] = 0
                continue

            if numberOfVals > 1:
                raise Exception(f'index {i} has more than one unique values. Stopping at {i}')

            if df.iloc[:, i].value_counts().index[0] != 1.0:
                raise Exception(f'index {i} has some value other than 1.0. Stopping at {i}')
            
            print(f'transforming column as it has no errors {i}')

            df.iloc[:, i] = np.where(df.iloc[:, i].isna(), 0,  df.iloc[:, i])

        return df