import pandas as pd
from app.pipeline.extract import extract_data
from app.pipeline.transform import concat_data_frames
from app.pipeline.load import load_df



def test_extract(): 
    # Test reading a CSV file that exists
    df = pd.read_csv('test_data.csv')
    df.assertIsNotNone(df)
    df.assertIsInstance(df, pd.DataFrame)

def test_transform():

    arrange = pd.concat([df_1, df_2], ignore_index=True)
    act = concat_data_frames([df_1, df_2])
    assert arrange == act


if __name__ == '__main__':
    # Test_transfor function parameters
    df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
    df_2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})
