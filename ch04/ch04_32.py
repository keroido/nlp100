#32. 動詞の原形Permalink
#動詞の原形をすべて抽出せよ．


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

def extractVerb(block, infs=False):
    res = list(filter(lambda x: x['pos'] == '動詞', block))
    if infs:
        res = [r['base'] for r in res]
    else:
        res = [r['surface'] for r in res]
    return res




filename = '../data/neko.txt.mecab'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = parseMecab(blockList[0])
ans = extractVerb(blockList, infs=True)
print(ans)
