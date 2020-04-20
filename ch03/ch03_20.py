import pandas as pd

df = pd.read_json('../data/jawiki-country.json', lines=True)
uk = df[df['title'] == 'イギリス']['text'].values[0]
print(uk)
