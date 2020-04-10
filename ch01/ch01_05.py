"""
02. n-gramPermalink
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

def word_n_gram(n, target):
    '''単語n-gram

    Args:
        n(int) : targetの長さ=len(target)
        target(str) : n-gramを得たい文字列

    Returns:
        ans(list) : n-gramに変換されたtarget(単語単位)
    '''
    lst = list(target.split(' '))
    if len(lst) < n: n = len(lst)
    ln = len(lst) - n + 1
    ans = []

    for i in range(ln):
        tmp = ''
        for j in range(n):
            tmp += lst[i+j] + '-'
        ans.append(tmp[:-1])

    return ans


def letter_n_gram(n, target):
    '''文字n-gram

    Args:
        n(int) : targetの長さ=len(target)
        target(str) : n-gramを得たい文字列

    Returns:
        ans(list) : n-gramに変換されたtarget(文字単位)
    '''
    lst = list(target)
    if len(lst) < n: n = len(lst)
    ln = len(lst) - n + 1
    ans = []

    for i in range(ln):
        ans.append(''.join(lst[i:i+n]))

    return ans


if __name__ == '__main__':
    print('----- letter n-gram -----')
    print();print('n: {}, target: {}'.format(1, 'I am an NLPer'))
    print(letter_n_gram(1, 'I am an NLPer'))
    print();print('n: {}, target: {}'.format(2, 'I am an NLPer'))
    print(letter_n_gram(2, 'I am an NLPer'))
    print();print('n: {}, target: {}'.format(3, 'I am an NLPer'))
    print(letter_n_gram(3, 'I am an NLPer'))

    print();print();print('----- word n-gram -----')

    print();print('n: {}, target: {}'.format(1, 'I am an NLPer'))
    print(word_n_gram(1, 'I am an NLPer'))
    print();print('n: {}, target: {}'.format(2, 'I am an NLPer'))
    print(word_n_gram(2, 'I am an NLPer'))
    print();print('n: {}, target: {}'.format(3, 'I am an NLPer'))
    print(word_n_gram(3, 'I am an NLPer'))
