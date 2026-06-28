# 一つの入力フィールドから内容によって保存する対象を分けたい場合

score = input("『点数』もしくは『ランク』を入力してください。")

if score.isdecimal():
    point = score
    rank = ""
else:
    point = 0
    rank = score
