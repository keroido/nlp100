#34. 名詞の連接Permalink
#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


def parseMecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        surface, attr = line.split('\t')
        attr = attr.split(',')
        lineDict = {
            'surface': surface,
            'base' : attr[6],
            'pos' : attr[0],
            'pos1' : attr[1]
        }
        res.append(lineDict)

def extractNoun_lmp(block):
    mx, now = 0, 0
    res, tmp = [], []
    tf = False
    for b in block:
        if tf is False and b['pos'] == '名詞':
            tmp.append(b['surface'])
            now = 1
            tf = True
        elif tf is True and b['pos'] == '名詞':
            tmp.append(b['surface'])
            now += 1
        elif tf is True and b['pos'] != '名詞':
            if now > mx:
                res = [''.join(tmp)]
                mx = now
            elif now == mx:
                res.append(''.join(tmp))
            tf = False
            tmp = []
            now = 0
    return res, mx







filename = '../data/neko.txt.mecab'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = parseMecab(blockList[0])
ans = extractNoun_lmp(blockList)
print(ans)
