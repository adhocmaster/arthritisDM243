import pandas as pd
import numpy as np
from library.ValueTransformer import ValueTransformer
from library.CategoryValueTransformer import CategoryValueTransformer

class OtherValueTransformer:


    def __init__(self):
        self.valueTransformer = ValueTransformer()
        self.categoryValueTransformer = CategoryValueTransformer()

    def transformOther(self, df: pd.DataFrame, otherTextCol):
        '''
        this needs to be a text column. For 0/1 type columns use ValueTransformer.fillMissingWith0
        '''

        return self.categoryValueTransformer.transform(df, otherTextCol)



    
    def transformOtherAndText(self, df: pd.DataFrame, otherCol, otherTextCol):

        # 1. Find categorical values
        # 2. if 1, fill with existing value. If value does not exist, fill with "Other"
        # 2. if no 1 or 0, fill with NA
        df = self.valueTransformer.fillMissingWith0(df, otherCol)
        df = self.transformOther(df, otherTextCol)
        return df
        