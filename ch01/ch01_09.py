"""
09. TypoglycemiaPermalink
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
"""

def mixer(sentence):
    """
    各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラム

    Args:
        sentence(str) : 英語の文章

    Returns:
        ans(str) : 返還後の英語の文章
    """
    from random import sample

    s = list(sentence.split())
    ss = []
    for i in s:
        ss.append(i)
        ss.append(' ')
    ss = ss[:-1]

    ans = ''
    for i in range(len(ss)):
        tmp = ''
        if len(ss[i]) > 4:
            tmp = ss[i][0] + ''.join(sample(ss[i][1:-1], len(ss[i][1:-1]))) + ss[i][-1]
        else:
            tmp = ss[i]
        ans += tmp

    return ans

if __name__ == '__main__':
    s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
    print(mixer(s))
