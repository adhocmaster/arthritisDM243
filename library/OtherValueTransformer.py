import pandas as pd
import numpy as np

class OtherValueTransformer:


    def transformOther(self, df: pd.DataFrame, otherCol):

        # 1. Find categorical values
        # 2. Find duplicates? (minimal case, strip spaces)
        # 3. Fill missing with NA



        return df



    
    def transformOtherAndText(self, df: pd.DataFrame, otherCol, otherTextCol):

        # 1. Find categorical values
        # 2. if 1, fill with existing value. If value does not exist, fill with "Other"
        # 2. if no 1 or 0, fill with NA
        return df
        