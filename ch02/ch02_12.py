#12. 1列目をcol1.txtに，2列目をcol2.txtに保存Permalink
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import os

path = '../data/popular-names.txt'

with open(path) as f:
    tmp = [i for i in f.read().split('\n') if i is not '']
    tmp = [list(i.split()) for i in tmp]

with open('../data/col1.txt', mode='w') as f:
    table = [i[0] for i in tmp]
    for r in table:
        f.write(r + '\n')

with open('../data/col2.txt', mode='w') as f:
    table = [i[1] for i in tmp]
    for r in table:
        f.write(r + '\n')
