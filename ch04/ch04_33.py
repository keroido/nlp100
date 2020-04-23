#33. 「AのB」Permalink
#2つの名詞が「の」で連結されている名詞句を抽出せよ．

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



def extractNounPhrase(block):
    res = []
    ln = len(block)
    for i in range(ln-2):
        if block[i]['pos'] == '名詞' and block[i+1]['surface'] == 'の' and block[i+2]['pos'] == '名詞':
            res.append(block[i]['surface'] + block[i+1]['surface'] + block[i+2]['surface'])
    return res




filename = '../data/neko.txt.mecab'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = parseMecab(blockList[0])
ans = extractNounPhrase(blockList)
print(ans)
