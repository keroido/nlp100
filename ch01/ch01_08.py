"""
08. 暗号文Permalink
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(sentence):
    """以下の仕様で変換する
    - 英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力

    Args:
        sentence(str) : 文章

    Returns:
        ans(str) : 変換後の文章
    """
    ans = ''
    for i in range(len(sentence)):
        if sentence[i].islower():
            ans += chr(219-ord(sentence[i]))
        else:
            ans += sentence[i]

    return ans


if __name__ == '__main__':
    print("I Am An Engineer.")
    print(); print('----- converted -----'); print()
    print(cipher("I Am An Engineer."))
