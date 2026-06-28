# 繰り返し処理(for文)
# イテラブルな要素に対して順番に値を1つずつ参照していく。


# 基本形
def loop_for_1():
    member = ["佐藤", "佐々木", "高橋", "中村"]
    for name in member:
        print(f"参加者名:{name}")


# rangeオブジェクトについて
# 変数の値を順番に変えながら処理する
def loop_for_2():
    # 基本的な書き方 range(stop)
    print("======range(stop)の書き方======")
    for a in range(10):
        print(a)
    # スタートを指定する場合　range(start,stop)
    print("===range(start,stop)の書き方===")
    for y in range(3, 9):
        print(y)
    # 間隔を指定する場合　range(start,stop,step)
    print("=range(start,stop,step)の書き方=")
    for z in range(1, 20, 5):
        print(z)


# ループの抜け方
# break　に当たるとループから抜けることができる
def loop_for_3():
    for i in range(100):
        print(f"iの値は{i}です")
        if i == 10:
            print("iの値が10になりました。")
            break


# ループ中の処理をスキップする
# continue　に当たるとそれ以降の処理を実行せず、次のループにいく
def loop_for_4():
    for i in range(31):
        if i % 2 == 0:
            continue
        print(f"{i}は奇数です。")


# ループする際に値とインデックスの両方を取りたい場合
# enumerate()
def loop_for_5():
    members = ["高橋", "田中", "木村", "佐藤"]
    # 第二引数で開始位置を指定することができる。
    for index, member in enumerate(members, start=1):
        print(f"{index}人目の名前は{member}です。")


# 複数のリストを同時にループさせたい場合
# zip()
def loop_for_6():
    members = ["高橋", "田中", "木村", "佐藤"]
    scores = [80, 90, 70, 60]
    for member, score in zip(members, scores):
        print(f"{member}さんの点数は{score}です")
