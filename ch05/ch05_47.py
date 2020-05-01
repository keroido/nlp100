#47. 機能動詞構文のマイニングPermalink
#動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

"""
- 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
- 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
- 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
"""

#例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

"""
返事をする      と に は        及ばんさと 手紙に 主人は
"""

#このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

"""
- コーパス中で頻出する述語（サ変接続名詞+を+動詞）
- コーパス中で頻出する述語と助詞パターン
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
with open('../data/ch05_47_result.txt', mode='w', encoding='utf-8') as f:
    for sentence in texts:
        ans, tmp1, tmp2 = [None, [], []], [], []
        for clause in sentence:
            for i in range(len(clause.morphs)):
                if clause.morphs[i].pos == '助詞' and clause.morphs[i].surface == 'を' and i > 0:
                    if clause.morphs[i-1].pos == '名詞' and clause.morphs[i-1].pos1 == 'サ変接続':
                        for j in range(len(sentence[int(clause.dst)].morphs)):
                            if sentence[int(clause.dst)].morphs[j].pos == '動詞' and sentence[int(clause.dst)].morphs[j].pos2 == '基本形':
                                ans[0] = ''.join([c.surface for c in clause.morphs]) + ''.join([c.surface for c in sentence[int(clause.dst)].morphs[:j+1]])
                                for src in sentence[int(clause.dst)].srcs:
                                    tmp1.append(''.join([c.base for c in sentence[int(src)].morphs if c.pos == '助詞']))
                                    tmp2.append(''.join([c.surface for c in sentence[int(src)].morphs]))
                                tmp3 = [i+' '+j for i, j in zip(tmp1[:-1], tmp2[:-1])]
                                tmp3.sort()
                                tmp1, tmp2 = [], []
                                for t in tmp3:
                                    ad = t.split(' ')
                                    tmp1.append(ad[0])
                                    tmp2.append(ad[1])
                                tmp1 = [t.replace('、', '') for t in tmp1]
                                tmp2 = [t.replace('、', '') for t in tmp2]
                                f.write(ans[0] + '\t' + ' '.join(tmp1) + '\t' + ' '.join(tmp2) + '\n')
                                #print(ans[0] + '\t' + ' '.join(tmp1) + '\t' + ' '.join(tmp2))
