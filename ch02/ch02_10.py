#10. 行数のカウントPermalink
#行数をカウントせよ．確認にはwcコマンドを用いよ．
import os

path = '../data/popular-names.txt'
with open(path) as f:
    print(len(f.read().split('\n')))

print('$ wc -l ../data/popular-names.txt')
os.system('wc -l ../data/popular-names.txt')
