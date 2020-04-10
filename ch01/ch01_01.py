"""
01. 「パタトクカシーー」Permalink
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""
ans = ''
s = 'パタトクカシーー'
for i in range(len(s)):
    if i%2 == 0:
        ans += s[i]
print(ans)
