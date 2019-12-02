import pandas as pd
import numpy as np
from library.ValueTransformer import ValueTransformer
from pprint import PrettyPrinter

class CategoryValueTransformer:


    def __init__(self, ignoreYesNoConversion = False):

        self.valueTransformer = ValueTransformer(ignoreYesNoConversion)
        self.printer = PrettyPrinter()

    def transform(self, df: pd.DataFrame, col):

        # 1. Find categorical values
        # 2. Find duplicates? (minimal case, strip spaces)

        df = self.valueTransformer.sanitizeTextCol(df, col)

        # 3. Fill missing with NA
        df = self.valueTransformer.fillMissingWithNA(df, col)
        # print(f'replacing na values with NA for {col}')
        # print(df[col].isna().sum())
        # print(id(df))

        return df

    def combineAndTransformWithSecond(self, df: pd.DataFrame, firstCol, secondCol):

        ''' Creates a new column 'combined_' + firstCol + '_' + secondCol '''

        newCol = 'combined_' + firstCol + '_' + secondCol

        # there second cols is not na, copy that value to first col
        df[newCol] = np.where(df[secondCol].isna(), df[firstCol], df[secondCol])
        return self.transform(df, newCol)


    def shortenCategoricalValues(self, df: pd.DataFrame, col):

        if isinstance(df[col][0], np.str) is False:
            print(f'skipping shortening for column {col} as it is not a string')
            return df

        minLengthForTransformation = 5
        uniqueVals = df[col].unique()
        uniqueMap = {}
        i = 1
        for val in uniqueVals:
            if len(val) >= minLengthForTransformation:
                uniqueMap[val] = 'cat-' + str(i)
            else:
                uniqueMap[val] = val

        print(f'generated transformation map for column {col}:')
        self.printer.pprint(uniqueMap)

        df[col] = df[col].transform( lambda x: uniqueMap[x])

        return df

    
    def findColumnsWithLongText( self, df: pd.DataFrame):

        minLen=10
        longCols = []
        for col in df.columns:

            if isinstance(df[col][0], np.str) is False:
                continue
            
            # print(f'{col} is not numeric')
            uniqueVals = df[col].unique()
            for val in uniqueVals:
                length = len(val)
                if length >= minLen:
                    print(f'Column {col} has a value {val} of length {length}')
                    longCols.append(col)
                    break
                pass
            pass
        
        self.printer.pprint(longCols)
        


        