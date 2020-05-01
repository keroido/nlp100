#48. 名詞から根へのパスの抽出Permalink
#文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

"""
- 各文節は（表層形の）形態素列で表現する
- パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
"""

#「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

"""
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

import CaboCha

class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']
        self.pos2 = dc['pos2']


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

    def appendSrc(self, src):
        self.srcs = src


def parse(block):
    tmp, srcs, res = {'morphs':[], 'dst':-1}, {}, []
    block = [b for b in block.split('\n') if b != ''] + ['']
    for b in block:
        if b == '':
            res.append(Chunk(tmp['morphs'], tmp['dst']))
            ln = len(res)
            for i in range(ln):
                if str(i) in srcs:
                    res[i].appendSrc(srcs[str(i)])
            return res
        elif b[0] == '*':
            if tmp['morphs'] != []:
                res.append(Chunk(tmp['morphs'], tmp['dst']))
            tmp = {'morphs':[], 'dst':-1}
            lst = b.split('D')[0].split(' ')
            tmp['dst'], now = lst[2], lst[1]
            if now != '-1':
                if tmp['dst'] in srcs:
                    srcs[tmp['dst']].append(now)
                else:
                    srcs[tmp['dst']] = [now]
        else:
            (surface, attr, _) = b.split('\t')
            attr = attr.split(',')
            lineDict = {
                'surface': surface,
                'base': attr[6],
                'pos': attr[0],
                'pos1': attr[1],
                'pos2': attr[5]
            }
            tmp['morphs'].append(Morph(lineDict))


filename = '../data/tmp.cabocha'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read().split('EOS')
texts = [parse(b) for b in blockList]

with open('../data/ch05_48_result.txt', mode='w', encoding='utf-8') as f:
    for sentence in texts:
        ans = []
        for clause in sentence:
            tmp, tf = '', True
            if '名詞' in [m.pos for m in clause.morphs] and int(clause.dst) > -1:
                tmp += ''.join([m.surface for m in clause.morphs]) + ' -> '
                dst = int(clause.dst)
                while tf:
                    tmp += ''.join([m.surface for m in sentence[dst].morphs]) + ' -> '
                    if int(sentence[dst].dst) > -1:
                        dst = int(sentence[dst].dst)
                    else:
                        tf = False
                        tmp = tmp[:-4]
                        tmp = tmp.replace('、', '').replace('。', '')
                ans.append(tmp)
        if ans != []:
            for line in ans:
                f.write(line + '\n')
            f.write('\n')
