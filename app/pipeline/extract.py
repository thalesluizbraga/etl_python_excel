#lista arquivos em excel
# jogar em dfs
# ter uma lista de dfs

import os # biblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos

import pandas as pd
from typing import List



path = '../data/input/' 

def extract_data(path: str) -> list[pd.DataFrame]:

    """
    Function which read .xlsx files in a folder and returns a list of dataframes.

    args: input_path (str): path to the folder with .xlsx files.

    return: list of dataframes.
    """
    
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    df_list = []

    for file in all_files: 
        data = pd.read_excel(file)
        df_list.append(data)

    return df_list   

if __name__ == '__main__':
    df_list = extract_data(path)
    print(df_list)