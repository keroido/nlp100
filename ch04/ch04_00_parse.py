import MeCab

t = MeCab.Tagger()
with open('../data/neko.txt') as f:
    text = f.read()
with open('../data/neko.txt.mecab', mode='w') as f:
    f.write(t.parse(text))
