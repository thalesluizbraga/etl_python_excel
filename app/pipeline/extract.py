#lista arquivos em excel
# jogar em dfs
# ter uma lista de dfs

import os # biblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos

import pandas as pd
from typing import List



def extract_data(path: str) -> list:

    """
    Function which read .xlsx files in a folder and returns a list of dataframes.

    args: input_path (str): path to the folder with .xlsx files.

    return: list of dataframes.
    """
    df_list = []
    for file in os.listdir(path):  
        if file.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(path, file))
            df_list.append(df)
    return df_list   

if __name__ == '__main__':
    path = '../data/input/' 
    df_list = extract_data(path)
    print(df_list)