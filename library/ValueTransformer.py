import pandas as pd

class ValueTransformer:


    def __init__(self):
        pass


    def getDiseasesMap(self):
        

        diseaseMap = {
            'Ankylosing Spondylitis': 'ankylosing', 
            'Still’s Disease': 'still',
            'Rheumatoid Arthritis': 'rheumatoid',
            'Undifferentiated Spondyloarthropathy (UsPA) *': 'UsPA',
            'Systemic Lupus Erythematosus': 'systemic' , 
            'Psoriatic Arthritis': 'psoriatic',
            'Undifferentiated Connective Tissue Disease (UCTD) *': 'UCTD',
            'Sjögren’s Syndrome': 'sjogren'
        }

        return diseaseMap

    def transformInitialDx(self, df: pd.DataFrame):

        diseaseMap = self.getDiseasesMap() 
        df['Initial_Dx'] = df['Initial_Dx'].transform( lambda x: diseaseMap[x])

        return df
    
    

