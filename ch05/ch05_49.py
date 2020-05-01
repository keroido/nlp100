#49. 名詞間の係り受けパスの抽出Permalink
#文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

"""
- 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を” -> “で連結して表現する
- 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．
- 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
- 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を” | “で連結して表示
"""

#例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

"""
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
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

with open('../data/ch05_49_result.txt', mode='w', encoding='utf-8') as f:
    for sentence in texts:
        noun_idx = [i for i in range(len(sentence)) if len([c for c in sentence[i].morphs if c.pos == '名詞']) > 0]
        if len(noun_idx) < 2:
            continue
        while len(noun_idx) >= 2:
            for i in noun_idx[1:]:
                dst = int(sentence[noun_idx[0]].dst)
                xlst = [noun_idx[0], dst]
                while dst > -1:
                    dst = int(sentence[dst].dst)
                    if dst > -1:
                        xlst.append(dst)
                dst = int(sentence[i].dst)
                ylst = [i, dst]
                while dst > -1:
                    dst = int(sentence[dst].dst)
                    if dst > -1:
                        ylst.append(dst)
                if ylst[0] in xlst:
                    tmp = [''.join(['X' if m.pos == '名詞' else m.surface for m in sentence[noun_idx[0]].morphs])]
                    if len(sentence[noun_idx[0]+1:i]) > 0:
                        tmp += [''.join([m.surface for m in c.morphs]) for c in sentence[noun_idx[0]+1:i]]
                    tmp += [''.join(['Y' if m.pos == '名詞' and j == 0 else m.surface  for m in c.morphs]) for j, c in enumerate(sentence[i:])]
                    ans = ' -> '.join(tmp)
                    ans = ans.split('Y')[0] + 'Y'
                    ans = ans.replace('。', '')
                    f.write(ans + '\n')
                else:
                    X = [''.join(['X' if m.pos == '名詞' else m.surface for m in sentence[noun_idx[0]].morphs])]
                    Y = [''.join(['Y' if m.pos == '名詞' and j == 0 else m.surface  for m in c.morphs]) for j, c in enumerate(sentence[i:])]
                    ans = ''.join(X) + ' | ' + ' -> '.join(Y)
                    ans = ans[::-1].replace('>-', '|', 1)
                    ans = ans[::-1]
                    ans = ans.replace('。', '')
                    f.write(ans + '\n')
            else:
                noun_idx = noun_idx[1:]

            #tmp = [''.join([m.surface for m in c.morphs]) for c in sentence[noun_idx[0]:]]







































"""
        xy_indices = [1 if len([c for c in sentence[i].morphs if c.pos == '名詞']) > 0 else 0 for i in range(len(sentence))]
        total = sum(xy_indices)
        ln = len(xy_indices)
        for i in range(ln):
            tmp = ''
            X, Y, K = False, False, False
            I, J = -1, -1
            if xy_indices[i] == 1 and total > 1:
                X = ''.join(['X' if c.pos == '名詞' else c.surface for c in sentence[i].morphs])
                xy_indices[i] = 0
                I = i
                for j in range(i+1, ln+1):
                    if xy_indices[j] == 1:
                        J = j
                        if sum(xy_indices[j:]) == 1:
                            Y = 'Y'
                        else:
                            Y = ''.join(['Y' if c.pos == '名詞' else c.surface for c in sentence[j].morphs])
                        break
                if Y != False:
                    break
            print(X, Y)
            if X != False and Y != False:
                xlst, ylst = [], []
                dst = int(sentence[I].dst)
                while dst > -1:
                    xlst.append(''.join([c.surface for c in sentence[dst].morphs]))
                    dst = int(sentence[dst].dst)
                dst = int(sentence[J].dst)
                while dst > -1:
                    ylst.append(''.join([c.surface for c in sentence[dst].morphs]))
                    dst = int(sentence[dst].dst)
                for x in xlst:
                    for y in ylst:
                        if x == y:
                            K = x
                            break
                    if K is False:
                        break

"""
