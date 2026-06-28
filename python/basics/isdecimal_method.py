# isdecimal()について

data = input("10進数ならTrue、それ以外ならFalseになります。")

if data.isdecimal():
    print(f"{data}は10進数です")
elif not data.isdecimal():
    print(f"{data}は10進数ではありません。")
