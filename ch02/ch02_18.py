#18. 各行を3コラム目の数値の降順にソートPermalink
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

#３列目の数値で降順にソートする？という理解で進める。

with open('../data/popular-names.txt') as f:
    tmp = [r.split() for r in f.read().split('\n') if not r is '']
    for r in tmp:
        r[2] = int(r[2])
    tmp.sort(key=lambda x: x[2], reverse=True)
    for r in tmp:
        r[2] = str(r[2])
    for r in tmp:
        l0 = r[0].ljust(16)
        l1 = r[1].ljust(4)
        l2 = r[2].ljust(10)
        l3 = r[3].ljust(10)
        print(l0 + l1 + l2 + l3)


# with open('../data/popular-names.txt') as f:
#     obj = f.read()
# rows = [row for row in obj.split('\n') if not row =='']
# ans = sorted(rows, key=lambda x:  -1 * float(x.split('\t')[2]))
# for r in ans:
#     print(r)
