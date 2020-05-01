import CaboCha

class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']

def parseCabocha(block):
    tmp, res = [], []
    for line in block:
        if line == '':
            res.append(tmp)
            return res
        elif line[0] == '*':
            continue
        surface, attr, _ = line.split('\t')
        attr = attr.split(',')
        lineDict = {
            'surface': surface,
            'base': attr[6],
            'pos': attr[0],
            'pos1': attr[1]
        }
        tmp.append(Morph(lineDict))
        if surface == '。':
            res.append(tmp)
            tmp = []

filename = '../data/tmp.cabocha'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read()
blockList = [b for b in blockList.split('\n') if b != '' and b != 'EOS'] + ['']
blockList = parseCabocha(blockList)
for b in blockList[2]:
    print(vars(b))
