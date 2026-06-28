# hasattr,getattr,setattrについて


class test:
    def __init__(self):
        self.name = "佐藤"
        self.age = "24"

    def print_info(self):
        print(f"私の名前は{self.name}です")


user = test()


class User:
    pass


class Job:
    pass


# === hasattrについて ===
"""
｟内容｠
オブジェクトの中に指定したアトリビュートが存在するか調べる組込み関数

｟書き方｠
hasattr(オブジェクト,アトリビュート名)

｟戻り値｠
Bool値
"""

print(hasattr(user, "name"))  # Trueになる
print(hasattr(user, "job"))  # Falseになる
print(hasattr(user, "print_info"))  # Trueになる


# === get_attr について ===
"""
｟内容｠
オブジェクトの中の指定したアトリビュートを取得する
※ .get()のオブジェクト版的な感じ

｟書き方｠#デフォルト値も設定できる。
getattr(オブジェクト,アトリビュート名,デフォルト値)

｟戻り値｠
アトリビュート
"""
print(getattr(user, "name"))  # 佐藤
print(getattr(user, "job", "無職"))  # 無職
print(
    getattr(user, "print_info")
)  # メソッドオブジェクトが返る。実行したい場合print_info()とする。


# === set_attr について ===
"""
｟内容｠
オブジェクトにアトリビュートをセットする

｟書き方｠
setattr(オブジェクト,アトリビュート名,値)

｟戻り値｠
None
※ 戻り値を受け取ってどうこうするわけじゃなくアトリビュートをセットするための関数
"""
setattr(user, "name", "田中")  # nameの値が佐藤から田中になる
setattr(
    user, "job", "エンジニア"
)  # user.job = "エンジニア"という新しいアトリビュートが追加される

print(user.name)  # 田中
print(user.age)  # 24
print(user.job)  # エンジニア


# Djangoプロジェクトのプロジェクトでよくみるsetattrの使われ方。
# (例)userというtestモデルのオブジェクトがあったとする
test_allow = ["name", "age"]  # testモデルのホワイトフィールド
info = {"name": "佐々木", "age": "25"}  # フロントなりから送られてきた情報という程
for key, value in info.items():
    if key in test_allow:
        setattr(user, key, value)  # アトリビュートがセットされる
    else:
        print("エラー")

user.save()  # 最後に保存する
