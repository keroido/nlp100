#27. 内部リンクの除去Permalink
#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import re
import pandas as pd

def remove_stress(d):
    r = re.compile("'+")
    return {k : r.sub('', v) for k, v in d.items()}

def remove_links(d):
    r = re.compile("(?:\[\[)?(.+?)(?:\]\])?")
    return {k : ''.join(r.findall(v)) for k, v in d.items()}


df = pd.read_json('../data/jawiki-country.json', lines=True)
uk = df[df['title'] == 'イギリス']['text'].values[0]
ukText = uk.split('\n')

p0 = re.compile('^\|+')
p1 = re.compile('\{\{基礎情報')
p2_p3 = re.compile('\|(.+?)=(.+)')
p4 = re.compile('\}\}')

ans, frg = {}, False
for r in ukText:
    if frg and p4.match(r):
        break
    if frg and p0.match(r):
        tmp = p2_p3.findall(r)[0]
        ans[tmp[0]] = tmp[1]
    if p1.match(r):
        frg = True

ans = remove_links(remove_stress(ans))

for k, v in ans.items():
    print(f'{k} : {v}')


# def remove_stress(dc):
#     r = re.compile("'+")
#     return {k: r.sub('', v) for k, v in dc.items()}
#
#
# def remove_inner_links(dc):
#     r = re.compile('\[\[(.+\||)(.+?)\]\]')
#     return {k: r.sub(r'\2', v) for k, v in dc.items()}


# df = pd.read_json('../data/jawiki-country.json', lines=True)
# ukText = df.query('title=="イギリス"')['text'].values[0]
#
# ls, fg = [], False
# template = '基礎情報'
# p1 = re.compile('\{\{' + template)
# p2 = re.compile('\}\}')
# p3 = re.compile('\|')
# p4 = re.compile('<ref(\s|>).+?(</ref>|$)')
# for l in ukText.split('\n'):
#     if fg:
#         ml = [p2.match(l), p3.match(l)]
#         if ml[0]:
#             break
#         if ml[1]:
#             ls.append(p4.sub('', l.strip()))
#     if p1.match(l):
#         fg = True
# p = re.compile('\|(.+?)\s=\s(.+)')
# ans = {m.group(1): m.group(2) for m in [p.match(c) for c in ls] if m != None}
# r = re.compile('\[\[(.+\||)(.+?)\]\]')
# ans = {k: r.sub(r'\2', v) for k, v in ans.items()}
# ans = remove_inner_links(remove_stress(ans))
#
# for k, v in ans.items():
#     print(f'{k} : {v}')


#日本語国名 : グレートブリテン及び北アイルランド連合王国
#公式国名 : {{lang|en|United Kingdom of Great Britain and Northern Ireland}}
#国旗画像 : Flag of the United Kingdom.svg
# 国章画像 : イギリスの国章
# 標語 : {{lang|fr|神と我が権利）
# 国歌 : [[ファイル:United States Navy Band - God Save the Queen.ogg}}
# 地図画像 : Europe-UK.svg
# 位置画像 : United Kingdom (+overseas territories) in the World (+Antarctica claims).svg
# 公用語 : 英語
# 首都 : ロンドン（事実上）
# 最大都市 : ロンドン
# 元首等肩書 : 女王
# 元首等氏名 : エリザベス2世
# 首相等肩書 : 首相
# 首相等氏名 : ボリス・ジョンソン
# 他元首等肩書1 : 貴族院議長
# 他元首等氏名1 : ノーマン・ファウラー
# 他元首等肩書2 : 庶民院議長
# 他元首等氏名2 : {{仮リンク|リンゼイ・ホイル|en|Lindsay Hoyle}}
# 他元首等肩書3 : 最高裁判所長官
# 他元首等氏名3 : ブレンダ・ヘイル
# 面積順位 : 76
# 面積大きさ : 1 E11
# 面積値 : 244,820
# 水面積率 : 1.3%
# 人口統計年 : 2018
# 人口順位 : 22
# 人口大きさ : 1 E7
# 人口値 : 6643万5600
# 人口密度値 : 271
# GDP統計年元 : 2012
# GDP値元 : 1兆5478億
# GDP統計年MER : 2012
# GDP順位MER : 6
# GDP値MER : 2兆4337億
# GDP統計年 : 2012
# GDP順位 : 6
# GDP値 : 2兆3162億
# GDP/人 : 36,727
# 建国形態 : 建国
# 確立形態1 : 1707年合同法まで）
# 確立年月日1 : 927年／843年
# 確立形態2 : グレートブリテン王国成立<br />（1707年合同法）
# 確立年月日2 : 1707年{{0}}5月{{0}}1日
# 確立形態3 : 1800年合同法）
# 確立年月日3 : 1801年{{0}}1月{{0}}1日
# 確立形態4 : 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
# 確立年月日4 : 1927年{{0}}4月12日
# 通貨 : UKポンド (£)
# 通貨コード : GBP
# 時間帯 : ±0
# 夏時間 : +1
# ISO 3166-1 : GB / GBR
# ccTLD : .uk / .gb
# 国際電話番号 : 44
# 注記 : <references/>
