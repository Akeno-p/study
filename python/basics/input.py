# === キーボードで入力した値を取る方法 ===

# inputで受け取った値は文字列(str)として扱われるので、実行結果は12になる。
def input_1():
    a = input("aの値を入力")
    b = input("bの値を入力")

    c = a + b
    print(c)


# 数値として計算したい場合、型を変更しよう(intやfloat)
def input_2():
    x = int(input("xの値を入力"))
    y = int(input("yの値を入力"))

    z = x + y
    print(z)