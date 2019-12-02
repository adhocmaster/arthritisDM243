import pandas as pd
import numpy as np

class ColumnProcessor:

    def dropSingleValuedColumns(self, df):

        # find single valued columns
        # print
        # drop

        singleCols = []

        for col in df.columns:
            if len(df[col].value_counts()) < 2:
                singleCols.append(col)

        print('removing single valued colums:')
        print(singleCols)

        for col in singleCols:
            df.drop(col, axis=1, inplace=True)

        return df
