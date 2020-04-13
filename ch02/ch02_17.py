#17. １列目の文字列の異なりPermalink
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

with open('../data/popular-names.txt') as f:
    names = [name.split()[0] for name in f.read().split('\n') if not name is '']
    names = list(set(names))
    names.sort()
    print(names)

import os
print()
# print('$ cat ../data/popular-names.txt | sed "s/\t/\ /g" | cut -f 1 -d " "  | sort | uniq')
# os.system('cat ../data/popular-names.txt | sed "s/\t/\ /g" | cut -f 1 -d " "  | sort | uniq')
