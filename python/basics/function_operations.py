# 関数


# 引数
def function_1(name="山田", age="20"):
    print(f"ユーザー名は{name}です")
    print(f"ユーザーは{age}歳です")


# 可変長引数(引数をタプルで受け取る)
def function_2(*members):
    for index, member in enumerate(members, start=1):
        print(f"{index}人目の名前は{member}です。")


# 可変長引数(引数を辞書で受け取る)
# 変数名 = キー　値 = 値　の辞書ができる
def function_3(**info):
    """
    実行するにはこのように書く。
    function_3(name="田中",age="24",job="エンジニア")

    このような辞書になる
    info = {
        "name" : "田中",
        "age" : "24",
        "job" : "エンジニア"
    }
    """
    info_items = info.items()
    for i, item in enumerate(info_items, start=1):
        print(f"{i}番目のアイテムは{item}です")


# 戻り値
def function_4(price):
    """
    return 戻り値

    と書くことで結果を受け取ることができます。

    vat = function_4(1000)
    print(f"消費税は{vat}円です")

    #実行結果
    消費税は100円です

    戻り値をタプルにすることで複数の値を戻すことができます

    """
    vat = int(price * 0.1)
    return vat
