# 辞書の操作

info = {"name": "田中", "age": 24, "favoritefood": "カレー"}


# 値の取得
def dict_operations_1():
    # 変数名[キー] で取得することができる。
    # キーが存在しない場合エラーになります。
    tanaka = info["name"]
    print(tanaka)

    # 変数名.get(キー)で取得することもできる
    # キーが存在しな場合 None を返します。また第二引数でデフォルト値を設定できます。
    tanaka = info.get("name")
    print(tanaka)


# キーの取得 .keys()
# イテラブルな要素が返ってくる
def dict_operations_2():
    info_keys = info.keys()
    for i, key in enumerate(info_keys, start=1):
        print(f"{i}番目のキーは{key}です")


# 値の取得 .values()
# イテラブルな要素が返ってくる
def dict_operations_3():
    info_values = info.values()
    for i, value in enumerate(info_values, start=1):
        print(f"{i}番目の値は{value}です")


# キーと値の取得 .items()
# (キー,値)の形のタプルがイテラブルな要素で返ってくる
def dict_operations_4():
    info_items = info.items()
    for i, item in enumerate(info_items, start=1):
        print(f"{i}番目のアイテムは{item}です")


# 要素の追加(変更)　辞書[キー] = 値
def dict_operations_5():
    print(f"追加前のinfo{info}")
    # 辞書に該当のキーがなければ新しく要素が追加され、すでにある場合は上書きされる
    info["job"] = "エンジニア"
    print(f"追加語のinfo{info}")


# 要素の削除　del 辞書[キー]
def dict_operations_6():
    print(f"削除前のinfo{info}")
    # キーがなかったらエラーになります
    del info["name"]
    print(f"削除語のinfo{info}")


# 要素の数を確認　len(辞書)
def dict_operations_7():
    info_len = len(info)
    print(info_len)


# キーの存在確認　in
def dict_operations_8():
    # 戻り値はBool
    is_age: bool = "age" in info
    print(is_age)
