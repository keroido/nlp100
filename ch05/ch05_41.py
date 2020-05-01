#41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
#40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

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
ans = [parse(b) for b in blockList]
for i, block in enumerate(ans[7]):
    print(f'index: {i}', [b.surface for b in block.morphs], block.dst, block.srcs)
