#13. col1.txtとcol2.txtをマージPermalink
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open('../data/col1.txt') as f:
    col1 = [r for r in f.read().split('\n') if not r is '']

with open('../data/col2.txt') as f:
    col2 = [r for r in f.read().split('\n') if not r is '']

with open('../data/meaged_col1_col2.txt', mode='w') as f:
    if len(col1) != len(col2):
        print('='*20); print('col1 is not equal col2')
        exit()
    for r1, r2 in zip(col1, col2):
        f.write(r1 + '\t' + r2 + '\n')
