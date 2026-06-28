# 比較演算子
# 戻り値はbool値を返す。

# 左辺と右辺が等しいか ==
def comparison_1():
    a = int(input("aの値を入力してください"))
    b = int(input("b値を入力してください"))

    c = a == b

    print(c)


# 左辺と右辺が等しくないか　!=
def comparison_2():
    d = int(input("dの値を入力してください"))
    e = int(input("dの値を入力してください"))

    f = d!= e

    print(f)

# 左辺が右辺より大きいか　>　※以上の場合は >=
def comparison_3():
    g = int(input("gの値を入力してください"))
    h = int(input("hの値を入力してください"))

    i = g > h

    print(i)

# 左辺が右辺より小さいか　< ※以下の場合は <=
def comparison_4():
    j = int(input("jの値を入力してください"))
    k = int(input("kの値を入力してください"))

    l = j < k

    print(l)


# 比較演算子の連結
def comparison_5():
    m = int(input("mの値を入力してください"))
    o = (m > 5) and (m < 10)
    # 上記の式を繋げて下記のように書くことができる。
    p = 5 < m < 10
    print(p)
    # この場合左から順番に評価されていく。 5<m　の比較をし、次に m<10　の比較をする。
