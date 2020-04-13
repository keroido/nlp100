#16. ファイルをN分割するPermalink
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

n = int(input('n分割: '))
with open('../data/popular-names.txt') as f:
    tmp = f.read().split('\n')
    tmp = [i for i in tmp if not i is '']
    ln = len(tmp)
    m = int(ln // n)
    if n > ln:
        print('{}以上に分割できません。'.format(ln))
        exit()
    for i in range(n):
        print('\n'*2); print('{}分割目'.format(i+1)); print('\n'*2)
        for r in tmp[i*m:(i+1)*m]:
            print(r)
    else:
        if ln%n != 0:
            print('\n'*2); print('{}分割目'.format(n+1)); print('\n'*2)
            for r in tmp[n*m:]:
                print(r)
