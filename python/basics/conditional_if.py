#  条件式(if文)について ====


# 1. elifで条件を増やせる。
def conditional_if_1():
    # elseはifやelifに当てはまらなかった場合の処理。

    age = int(input("入力"))

    if age >= 20:
        print("成人しています。")
    elif age >= 18:
        print("成人していますが、お酒は飲んでいけません")
    else:
        print("成人していません。")


# 2. if文はBool値で結果を評価している。
def conditional_if_2():
    test = True

    if test:
        print("Bool値がTrueなのでこの条件が走る。")


# 3. 三項演算子
# ifとelseによって条件を分ける時、1行で書くことができる。
# 式：【変数 = 成功時の値 if 条件式 else 失敗時の値。】


# 通常の書き方
def conditional_if_3():
    age = 21
    if age >= 20:
        result = "成人です"
    else:
        result = "成人ではありません。"
    print(result)


# 三項演算子を使った書き方
def conditional_if_4():
    age = input("年齢を入力してください")
    result = "成人です" if age >= 20 else "成人ではありません"
    print(result)


# 4. Bool以外で評価されるものについて(Truthy)
# True/False以外にも評価される対象になる値がある。


def conditional_if_5():
    # Falseとして扱われるもの
    # 0, "", [], {}, (), None
    # ｟例｠
    if 0:
        print("実行されない")

    if []:
        print("実行されない")

    # Trueとして扱われるもの
    # 1以上の数値, "hello", [1,2,3], {"key": "value"}
    # ｟例｠
    if 10:
        print("実行される")
    if [1, 2, 3]:
        print("実行される")
