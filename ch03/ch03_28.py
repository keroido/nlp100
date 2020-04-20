#28. MediaWikiマークアップの除去Permalink
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import re
import pandas as pd

def remove_stress(d):
    r = re.compile("'+")
    return {k : r.sub('', v) for k, v in d.items()}

def remove_links(d):
    r = re.compile("(?:\[\[)?(.+?)(?:\]\])?")
    return {k : ''.join(r.findall(v)) for k, v in d.items()}

def remove_mu(d):
    r1 = re.compile('{{|}}')
    r2 = re.compile('<br />')
    r3 = re.compile('</?ref(.+)?>')
    r4 = re.compile('ファイル:.+?\|.+?\|')
    return {k: r1.sub('', r2.sub('', r3.sub('', r4.sub('', v)))) for k, v in d.items()}





df = pd.read_json('../data/jawiki-country.json', lines=True)
uk = df[df['title'] == 'イギリス']['text'].values[0]
ukText = uk.split('\n')

p0 = re.compile('^\|+')
p1 = re.compile('\{\{基礎情報')
p2_p3 = re.compile('\|(.+?)=(.+)')
p4 = re.compile('\}\}')

ans, frg = {}, False
for r in ukText:
    if frg and p4.match(r):
        break
    if frg and p0.match(r):
        tmp = p2_p3.findall(r)[0]
        ans[tmp[0]] = tmp[1]
    if p1.match(r):
        frg = True

ans = remove_mu(remove_links(remove_stress(ans)))

for k, v in ans.items():
    print(f'{k} : {v}')
