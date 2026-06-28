# クラス

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name}：ユーザー名")
        print(f"{self.age}：年齢")

name = input("ユーザー名を入力してください")
age = input("年齢を入力してください")

user = Student(name,age)


# 継承
# クラス名の後ろに()をつけて継承したいクラスを記述する
class NewClass(Student):
    pass


# クラスの属性を書き換える方法
user.name = "これで上書き"


# 毎回呼ぶ処理について
class Test:
    def __init__(self):
        self.name = "テスト"
        self.age = 24
    
    def __call__(self):
        print(f"{self.name}さんは{self.age}歳です")

    def set_info(self):
        name = input("ユーザー名を入力してください")
        age = input("年齢を入力してください")
        self.name = name
        self.age = age

test = Test()
test()