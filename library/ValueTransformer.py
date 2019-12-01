import pandas as pd
import numpy as np

from library.DiseaseTransformer import DiseaseTransformer

class ValueTransformer:


    def __init__(self):
        self.diseaseTransformer = DiseaseTransformer()
        pass


    def transformInitialDx(self, df: pd.DataFrame):

        return self.diseaseTransformer.transformInitialDx(df)

    
    def transformDx_Chosen(self, df: pd.DataFrame):

        return self.diseaseTransformer.transformDx_Chosen(df)


    def sanitizeTextCol(self, df:pd.DataFrame, col):
        df[col] = df[col].str.strip().str.lower().str.replace('  ', ' ').str.replace(' ', '_').str.replace('+', 'plus').str.replace('/', '').str.replace('(', '').str.replace(')', '').str.replace('[', '').str.replace(']', '')
        return df


    def fillMissingWithNA(self, df:pd.DataFrame, col):
        df[col] = np.where(df[col].isna(), 'NA',  df[col])
        return df

    def fillMissingWith0(self, df:pd.DataFrame, col):
        df[col] = np.where(df[col].isna(), 0,  df[col])
        return df
    

    def convertNumericToStr(self, df:pd.DataFrame, col, prefix='s'):
        df[col] = prefix + df[col].astype('str')

    def convert01ToYesNo(self, df:pd.DataFrame, col):
        df[col] = np.where(df[col] == 0, 'no',  'yes')
        return df

    

