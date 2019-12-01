import pandas as pd
import numpy as np

from library.DiseaseTransformer import DiseaseTransformer

class ValueTransformer:


    def __init__(self):
        self.diseaseTransformer = DiseaseTransformer()

        self.firbroMap = {
            'No, I have never been diagnosed with fibromyalgia.': 'No',
            'Yes, I was diagnosed with fibromyalgia after my Autoimmune Arthritis diagnosis. Please specify month/year of diagnosis:': 'No',
            'Yes, I was diagnosed with fibromyalgia prior to my Autoimmune Arthritis diagnosis and I do, in fact, have fibromyalgia in addition to my Autoimmune Arthritis disease.': 'Yes',
            'Yes, I was diagnosed with fibromyalgia prior to my Autoimmune Arthritis diagnosis, however, it was later determined that I do not have fibromyalgia.': 'Yes',
        }
        pass


    def transformInitialDx(self, df: pd.DataFrame):

        return self.diseaseTransformer.transformInitialDx(df)

    
    def transformDx_Chosen(self, df: pd.DataFrame):

        return self.diseaseTransformer.transformDx_Chosen(df)

    
    def transformFibro(self, df: pd.DataFrame):
        
        diseaseMap = self.firbroMap
        df['Fibro_dx'] = df['Fibro_dx'].transform( lambda x: diseaseMap[x])

        return df


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

    

