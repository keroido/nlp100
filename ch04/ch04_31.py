#31. 動詞Permalink
#動詞の表層形をすべて抽出せよ．

def parseMecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        (surface, attr) = line.split('\t')
        attr = attr.split(',')
        lineDict = {
            'surface': surface,
            'base' : attr[6],
            'pos' : attr[0],
            'pos1' : attr[1]
        }
        res.append(lineDict)


def extractVerb(block):
    res = list(filter(lambda x: x['pos'] == '動詞', block))
    res = [r['surface'] for r in res]
    return res




filename = '../data/neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = list(filter(lambda x: x != '', blockList))
blockList = [parseMecab(block) for block in blockList]

ans = extractVerb(blockList[0])
print(ans)

