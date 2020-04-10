"""
03. 円周率Permalink
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = list(text.split(' '))
ans = []
for s in text:
    ans.append(s[0])
print(ans)
