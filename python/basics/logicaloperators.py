# 論理演算子

# 両方がTrueの時(and)
def logicaloperators_1():
    user = {"ID":"test","PASS":"123"}
    user_id = input("IDを入力してください")
    user_pass = input("パスワードを入力してください")  

    if user.get("ID") == user_id and user.get("PASS") == user_pass:
        print("ログインに成功しました。")
    else:
        print("ログインに失敗しました。")



# どれか一つでもTrue(or)
def logicaloperators_2():
    yomikata = input("｟重複｠の読み方を入力してください")

    if yomikata == "ちょうふく" or yomikata =="じゅうふく":
        print("正しい読み方です")
    else:
        print("読み方が間違っています")



# Falseの場合(not)
def logicaloperators_3():
    name = input("名前を入力してください")

    if not name:
        print("名前が入力されていません。")
    else:
        print(f"あなたの名前は{name}です。")
    # ポイント!
    # ↓比較演算子を使用したら同じように書くことはできるが、その場合コードが見づらい。
    if name == "":
        print("名前が入力されていません")

