import pandas as pd
import numpy as np
from library.ValueTransformer import ValueTransformer

class CategoryValueTransformer:


    def __init__(self):
        self.valueTransformer = ValueTransformer()

    def transform(self, df: pd.DataFrame, col):

        # 1. Find categorical values
        # 2. Find duplicates? (minimal case, strip spaces)

        df = self.valueTransformer.sanitizeTextCol(df, col)

        # 3. Fill missing with NA
        df = self.valueTransformer.fillMissingWithNA(df, col)

        return df

    def combineAndTransformWithSecond(self, df: pd.DataFrame, firstCol, secondCol):

        ''' Creates a new column 'combined_' + firstCol + '_' + secondCol '''

        newCol = 'combined_' + firstCol + '_' + secondCol

        # there second cols is not na, copy that value to first col
        df[newCol] = np.where(df[secondCol].isna(), df[firstCol], df[secondCol])
        return self.transform(df, newCol)


        