#14. 先頭からN行を出力Permalink
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

n = int(input('何行出力するか: '))
with open('../data/popular-names.txt') as f:
    tmp = f.read().split('\n')[:n]
    for r in tmp:
        print(r)

import os
print()
print('$ head -n 5 ../data/popular-names.txt')
os.system('head -n 5 ../data/popular-names.txt')
