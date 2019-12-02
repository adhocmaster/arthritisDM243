import pandas as pd
import numpy as np

from library.DiseaseTransformer import DiseaseTransformer

class ValueTransformer:


    def __init__(self, ignoreYesNoConversion = False):

        self.ignoreYesNoConversion = ignoreYesNoConversion
        self.diseaseTransformer = DiseaseTransformer()

        self.firbroMapFirstDx = {
            'no,_i_have_never_been_diagnosed_with_fibromyalgia.': 'No',
            'yes,_i_was_diagnosed_with_fibromyalgia_after_my_autoimmune_arthritis_diagnosis._please_specify_monthyear_of_diagnosis:': 'No',
            'yes,_i_was_diagnosed_with_fibromyalgia_prior_to_my_autoimmune_arthritis_diagnosis_and_i_do,_in_fact,_have_fibromyalgia_in_addition_to_my_autoimmune_arthritis_disease.': 'Yes',
            'yes,_i_was_diagnosed_with_fibromyalgia_prior_to_my_autoimmune_arthritis_diagnosis,_however,_it_was_later_determined_that_i_do_not_have_fibromyalgia.': 'Yes',
        }
        self.firbroMapSecondDx = {
            'no,_i_have_never_been_diagnosed_with_fibromyalgia.': 'Never',
            'yes,_i_was_diagnosed_with_fibromyalgia_after_my_autoimmune_arthritis_diagnosis._please_specify_monthyear_of_diagnosis:': 'AfterFirst',
            'yes,_i_was_diagnosed_with_fibromyalgia_prior_to_my_autoimmune_arthritis_diagnosis_and_i_do,_in_fact,_have_fibromyalgia_in_addition_to_my_autoimmune_arthritis_disease.': 'BeforeFirst',
            'yes,_i_was_diagnosed_with_fibromyalgia_prior_to_my_autoimmune_arthritis_diagnosis,_however,_it_was_later_determined_that_i_do_not_have_fibromyalgia.': 'BeforeFirstFalsePositive',
        }
        pass


    def transformInitialDx(self, df: pd.DataFrame):

        return self.diseaseTransformer.transformInitialDx(df)

    
    def transformDx_Chosen(self, df: pd.DataFrame):

        return self.diseaseTransformer.transformDx_Chosen(df)

    
    def transformFibro(self, df: pd.DataFrame):
        
        firbroMapFirstDx = self.firbroMapFirstDx
        df['Fibro_dx_first'] = df['Fibro_dx'].transform( lambda x: firbroMapFirstDx[x])

        firbroMapSecondDx = self.firbroMapSecondDx
        df['Fibro_dx_second'] = df['Fibro_dx'].transform( lambda x: firbroMapSecondDx[x])

        

        return df


    def sanitizeTextCol(self, df:pd.DataFrame, col):
        df[col] = df[col].str.strip().str.lower().str.replace('  ', ' ').str.replace(' ', '_').str.replace('+', 'plus').str.replace('/', '').str.replace('(', '').str.replace(')', '').str.replace('[', '').str.replace(']', '')
        return df


    def fillMissingWithNA(self, df:pd.DataFrame, col):
        # df[col] = np.where(df[col].isna(), 'NA2',  df[col])
        df[col].fillna('NA2', inplace=True)
        return df

    def fillMissingWith0(self, df:pd.DataFrame, col):
        # df[col] = np.where(df[col].isna(), 0,  df[col])
        df[col].fillna(0, inplace=True)
        return df
    

    def convertNumericToStr(self, df:pd.DataFrame, col, prefix='s'):
        df[col] = prefix + df[col].astype('str')

    def convert01ToYesNo(self, df:pd.DataFrame, col):
        df = self.fillMissingWith0(df, col)
        if self.ignoreYesNoConversion:
            return df
        df[col] = np.where(df[col] == 0, 'no',  'yes')
        return df

    

