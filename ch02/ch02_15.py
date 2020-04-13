#15. 末尾のN行を出力Permalink
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

n = int(input('下から何行目までを出力するか：'))
with open('../data/popular-names.txt') as f:
    tmp = f.read().split('\n')
    tmp = tmp[len(tmp)-n-1:]
    for r in tmp:
        print(r)

import os
print()
print('$ tail -n 5 ../data/popular-names.txt')
os.system('tail -n 5 ../data/popular-names.txt')
