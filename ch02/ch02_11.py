#11. タブをスペースに置換Permalink
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
import os

path = '../data/popular-names.txt'
with open(path) as f:
    print(f.read().replace('\t', ' '))

#os.system('cat ../data/popular-names.txt | tr "\t" "\ "')
