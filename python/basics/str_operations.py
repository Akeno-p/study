# 文字列の操作


# 小文字への変換 lower()
def str_operations_1():
    name = "TANAKA"
    name_komoji = name.lower()
    print(f"{name_komoji}：これは小文字")


# 大文字への変換 upper()
def str_operations_2():
    name = "tanaka"
    name_oomoji = name.upper()
    print(f"{name_oomoji}：これは大文字")


# 分割処理 split()
# 引数で渡された文字で区切ったリストが返される
def str_operations_3():
    dates = "2024/03/01-2024/03/02-2024/03/03"
    date_list = dates.split("-")
    print(type(date_list))
    for date in date_list:
        print(f"{date}日")


# 置換 replace()
# 第一引数で渡した文字列が含まれる場合、第二引数で渡された文字列に置き換える
def str_operations_4():
    members = [
        {"name": "木村", "curriculums": "算数"},
        {"name": "佐藤", "curriculums": "数学"},
        {"name": "高橋", "curriculums": "日本史"},
        {"name": "中野", "curriculums": "英語"},
        {"name": "佐々木", "curriculums": "算数"},
    ]
    for member in members:
        print(
            f'{member.get("name")}さんは'
            f'{member.get("curriculums").replace("算数","数学")}が得意教科です。'
        )


# 整形 format()
# {}の場所に引数で指定した文字列を埋め込む。
def str_operations_5():
    year = 2026
    month = 3
    day = 28
    # 順番に{}に入れられていく
    message_1 = "今日は{}年{}月{}日です。".format(year, month, day)
    # {}にインデックス番号を書くことで指定することができる
    message_2 = "今日は{1}年{2}月{0}日です。".format(day, year, month)
    print(message_1)
    print(message_2)


# strip()
# 文字列の前後の文字を削除する
def str_operations_6():
    # 文字列の最初と最後の空欄を除去してくれる。
    name = input("名前を入力してください。")
    print(name)
    strip_name = name.strip()
    print(strip_name)

    # 引数を指定すると削除対象が引数で指定したものになる。。
    eng_name = input("英語で名前を入力してください。")
    print(f"{eng_name}：削除される前")
    delete_text = input("削除したいアルファベット(削除は最初と最後に対してだけ)")
    format_eng_name = eng_name.strip(delete_text)
    print(f"{format_eng_name}：指定したアルファベットが削除されたもの。")


# startswith()
# その文字列から始まる場合True
def str_operations_7():
    locations = {
        "tokyo": "1",
        "osaka": "2",
        "kyoto": "3",
        "okinawa": "4",
    }
    # 会員番号が(2-2222-22)みたいな形式の時に最初の桁が所在地を表すものとする
    member_number = input("会員番号を入力してください")

    for l, n in locations.items():
        if member_number.startswith(n):
            print(f"住所は{l}です。")
            break
