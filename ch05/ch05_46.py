#46. 動詞の格フレーム情報の抽出Permalink
#45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

"""
- 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
- 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
"""

#「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

"""
始める  で      ここで
見る    は を   吾輩は ものを
"""

import CaboCha

class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']


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
                'pos1': attr[1]
            }
            tmp['morphs'].append(Morph(lineDict))


filename = '../data/tmp.cabocha'
with open(filename, mode='r', encoding='utf-8') as f:
    blockList = f.read().split('EOS')
texts = [parse(b) for b in blockList]

with open('../data/ch05_46_result.txt', mode='w', encoding='utf-8') as f:
    for sentence in texts:
        ans = [None, []]
        for clause in sentence:
            for c in clause.morphs:
                if c.pos == '動詞':
                    ans[0] = c.base
                    allClause = ''
                    for i in clause.srcs:
                        for j in sentence[int(i)].morphs:
                            if j.pos == '助詞':
                                ans[1].append(j.base)
                                allClause += ''.join([c.surface for c in sentence[int(i)].morphs]) + ' '
                    else:
                        verb = ans[0]
                        pol = ans[1]
                        f.write(f'{verb}' + '   ' + ' '.join(pol) + '   '+ allClause + '\n')
                        ans = [None, []]
