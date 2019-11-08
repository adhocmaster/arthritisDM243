import pandas as pd
import numpy as np


class MVTransformer:

    """This class is meant to be used after value transformation as missing values may use values from other columns.
    
    Returns:
        [type] -- [description]
    """

    def __init__(self):
        pass


    def fixDx_Chosen(self, df: pd.DataFrame):

        """Expects Initial_Dx are transformed into codes and column names are fixed
        """
        df['Dx_Chosen'] = np.where(df.Dx_Chosen.isna(), df.Initial_Dx, df.Dx_Chosen)

        return df