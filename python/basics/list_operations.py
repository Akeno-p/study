# リストの操作


# === メソッドによる操作 ===

members = ["高橋", "田中", "木村", "佐藤"]


# 末尾に追加する append()
def list_operations_1():
    new_member = input("新しいメンバーを入力してください")
    members.append(new_member)
    print(members)


# 指定の位置に要素を追加する insert()
# 第一引数がインデックスの位置
def list_operations_2():
    new_member_name = input("新しいメンバーを入力してください")
    new_member_number = int(input("何番目に挿入したいですか？")) - 1
    members.insert(new_member_number, new_member_name)
    print(members)


# 指定したインデックスの要素を返しつつ削除　pop()
# インデックスを指定しなかった場合末尾の要素を削除します
def list_operations_3():
    members.pop(1)
    print(members)


# 対象の要素のインデックスを調べる　index()
def list_operations_4():
    member = input("調べたいメンバーを入力してください")
    member_index = members.index(member)
    print(member_index)


# 例 popとindexを組み合わせる
def list_operations_sample():
    delete_member = input("削除したいメンバーを入力してください")
    delete_index = members.index(delete_member)
    members.pop(delete_index)
    print(f"削除後のメンバーリスト{members}")


# リストの要素を全削除　clear()
def list_operations_5():
    print(f"削除された前のリスト → {members}")
    members.clear()
    print(f"削除された後のリスト → {members}")


# === メソッド以外の操作 ===


# 特定の要素を削除 del
# del 要素[インデックス]　と書く
def list_operations_6():
    print(f"削除前のリスト → {members}")
    del members[1]
    print(f"削除後のリスト → {members}")


# リストの連結 +
def list_operations_7():
    members_2 = ["伊藤", "金子", "竹内", "一ノ瀬"]
    new_members = members + members_2
    print(new_members)


# 要素が含まれているか確認する in
def list_operations_8():
    member = input("メンバーを入力してください")
    if member in members:
        print(f"{member}はリストに含まれます。")
    else:
        print(f"{member}はリストに含まれません。")


# 要素の数を調べる len()
def list_operations_9():
    print(f"要素数は{len(members)}です")


# リスト内包表記
# 【リスト名 = [式 for 変数 in イテラブルオブジェクト]】と書くことができる
def list_operations_10():
    members_index = []
    # 通常の書き方
    for member in members:
        member_index = members.index(member)
        members_index.append(member_index)
    print("=== 通常の書き方 ===")
    print(members_index)

    # リスト内包表記
    members_index2 = [members.index(member) for member in members]
    print("=== リスト内包表記 ===")
    print(members_index2)

    # 補足：条件式をつけることもできる
    members_index3 = [members.index(member) for member in members if member == "高橋"]
    print("=== リスト内包表記｟条件式あり｠ ===")
    print(members_index3)
