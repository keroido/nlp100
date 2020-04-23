#35. 単語の出現頻度Permalink
#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

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

def sortWord(block):
    res = {}
    for b in block:
        if not b['surface'] in res:
            res[b['surface']] = 1
        else:
            res[b['surface']] += 1
    return sorted(res.items(), key=lambda x: x[1], reverse=True)



filename = '../data/neko.txt.mecab'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = parseMecab(blockList[0])
ans = sortWord(blockList)
print(ans)
