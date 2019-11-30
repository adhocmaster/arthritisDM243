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


    

    

