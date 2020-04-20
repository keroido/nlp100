#21. カテゴリ名を含む行を抽出Permalink
#記事中でカテゴリ名を宣言している行を抽出せよ．

import pandas as pd

df = pd.read_json('../data/jawiki-country.json', lines=True)
uk = df[df['title'] == 'イギリス']['text'].values[0]
textLines = uk.split('\n')
ans = list(filter(lambda x: 'Category:' in x, textLines))
for a in ans:
    print(a)
