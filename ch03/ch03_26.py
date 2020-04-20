#26. 強調マークアップの除去Permalink
#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import re
import pandas as pd

def remove_stress(d):
    r = re.compile("'+")
    return {k : r.sub('', v) for k, v in d.items()}


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

ans = remove_stress(ans)
for k, v in ans.items():
    print(f'{k} : {v}')


 # 日本語国名 : グレートブリテン及び北アイルランド連合王国
 # 公式国名 : {{lang|en|United Kingdom of Great Britain and Northern Ireland}}
 # 国旗画像 : Flag of the United Kingdom.svg
 # 国章画像 : [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]
 # 標語 : {{lang|fr|[[Dieu et mon droit]]}}<br />（[[フランス語]]:[[Dieu et mon droit|神と我が権利]]）
 # 国歌 : [[女王陛下万歳|{{lang|en|God Save the Queen}}]]{{en icon}}<br />神よ女王を護り賜え<br />{{center|[[ファイル:United States Navy Band - God Save the Queen.ogg]]}}
 # 地図画像 : Europe-UK.svg
 # 位置画像 : United Kingdom (+overseas territories) in the World (+Antarctica claims).svg
 # 公用語 : [[英語]]
 # 首都 : [[ロンドン]]（事実上）
 # 最大都市 : ロンドン
 # 元首等肩書 : [[イギリスの君主|女王]]
 # 元首等氏名 : [[エリザベス2世]]
 # 首相等肩書 : [[イギリスの首相|首相]]
 # 首相等氏名 : [[ボリス・ジョンソン]]
 # 他元首等肩書1 : [[貴族院 (イギリス)|貴族院議長]]
 # 他元首等氏名1 : [[:en:Norman Fowler, Baron Fowler|ノーマン・ファウラー]]
 # 他元首等肩書2 : [[庶民院 (イギリス)|庶民院議長]]
 # 他元首等氏名2 : {{仮リンク|リンゼイ・ホイル|en|Lindsay Hoyle}}
 # 他元首等肩書3 : [[連合王国最高裁判所|最高裁判所長官]]
 # 他元首等氏名3 : [[:en:Brenda Hale, Baroness Hale of Richmond|ブレンダ・ヘイル]]
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
 # 確立形態1 : [[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[合同法 (1707年)|1707年合同法]]まで）
 # 確立年月日1 : 927年／843年
 # 確立形態2 : [[グレートブリテン王国]]成立<br />（1707年合同法）
 # 確立年月日2 : 1707年{{0}}5月{{0}}1日
 # 確立形態3 : [[グレートブリテン及びアイルランド連合王国]]成立<br />（[[合同法 (1800年)|1800年合同法]]）
 # 確立年月日3 : 1801年{{0}}1月{{0}}1日
 # 確立形態4 : 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
 # 確立年月日4 : 1927年{{0}}4月12日
 # 通貨 : [[スターリング・ポンド|UKポンド]] (£)
 # 通貨コード : GBP
 # 時間帯 : ±0
 # 夏時間 : +1
 # ISO 3166-1 : GB / GBR
 # ccTLD : [[.uk]] / [[.gb]]
 # 国際電話番号 : 44
 # 注記 : <references/>
