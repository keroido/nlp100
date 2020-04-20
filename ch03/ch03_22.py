#22. カテゴリ名の抽出Permalink
#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import pandas as pd

df = pd.read_json('../data/jawiki-country.json', lines=True)
uk = df[df['title'] == 'イギリス']['text'].values[0]
textLines = uk.split('\n')
category = list(filter(lambda x: 'Category:' in x, textLines))
ans = [r.replace('[[Category:', '').replace(']]', '').replace('|*', '') for r in category]
for a in ans:
    print(a)
