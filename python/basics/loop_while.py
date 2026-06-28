# 繰り返し処理(while文)
# 条件式に対してTrueの限りループが続く。
# breakでに当たったらループから抜ける。

# 基本的な形
def loop_while_1():
    i = 0
    while i < 5:
        print(f"iの値は{i}です")
        i += 1


# breakを使用した形
def loop_while_2():
    retry = 0
    while retry < 3:
        # response = api_call()
        #if response.success:
        #    break
        print(f"{retry}回目のアクセスに失敗しました")
        retry += 1

# 補足
# 2のようなコードを書く場合、連続で3回アクセスしてもあまり意味ないので少し時間を置きたい。
# そこで time.sleep()を使用すると時間を置くことができる。
def loop_while_3():
    import time
    retry = 0
    while retry < 3:
        # response = api_call()
        # if response.success:
        #     break
        print(f"{retry}回目のアクセスに失敗しました")
        retry += 1
        time.sleep(10) # これで10秒待つ



