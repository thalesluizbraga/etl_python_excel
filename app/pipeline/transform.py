import pandas as pd
from typing import List

"""
Função para transformar uma lista de dataframes em um unico dataframe.

"""

def concat_data_frames(df_list : list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(df_list, ignore_index=True)