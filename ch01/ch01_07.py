"""
07. テンプレートによる文生成Permalink
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
"""

def template_sentence(x, y, z):
    """定型文を返す関数
    「 x 時の y は z 」

    Args:
        x(int) : 時間
        y(str) : 例えば「気温」
        z(float) : 気温であれば22.4など

    Returns:
        ans(str) : x時のyはz　の定型文
    """

    return '{}時の{}は{}'.format(x, y, z)

if __name__ == '__main__':
    print('x 時の y は z')
    x = input('x: ')
    y = input('y: ')
    z = input('z: ')
    print(template_sentence(x, y, z))
