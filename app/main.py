from pipeline.extract import extract_data

path = '../data/input/'
df = extract_data(path)
print(df)