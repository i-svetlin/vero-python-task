import pandas as pd

with open('downloaded1.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('downloaded1.csv', encoding='utf-8', index=False)