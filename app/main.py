from pipeline.extract import extract_data
from pipeline.transform import concat_data_frames
from pipeline.load import load_df


if __name__ == '__main__':
    path = '../data/input/'
    df_list = extract_data(path)
    df = concat_data_frames(df_list)
    load_df(df,'data/output', 'file_loaded')
   