import CaboCha

c = CaboCha.Parser()
with open('../data/neko.txt', mode='r', encoding='utf-8') as f:
    text = f.read()
with open('../data/tmp.cabocha', mode='w', encoding='utf-8') as f:
    for se in [s + '。' for s in text.split('。')]:
        f.write(c.parse(se).toString(CaboCha.FORMAT_LATTICE))
