#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

with open('../data/popular-names.txt') as f:
    tmp = [r.split() for r in f.read().split('\n') if not r is '']
    names = [r[0] for r in tmp]
    unique_names = list(set(names))
    ans = {}
    for i in unique_names:
        ans[i] = 0
    for n in names:
        ans[n] += 1
    ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)
    for n in ans:
        print(n)

# import os
# print()
# print('$ cat ../data/popular-names.txt | sed "s/\t/\ /g" | cut -f 1 -d " " | sort | uniq -c | sort -rn -k 3 -t " "')
# os.systemu('cat ../data/popular-names.txt | sed "s/\t/\ /g" | cut -f 1 -d " " | sort | uniq -c | sort -rn -k 3 -t " "')
