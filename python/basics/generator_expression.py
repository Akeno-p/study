# 内包表記で書いた場合

naihouhyouki = [x % 2 == 0 for x in range(100)]  # この時点で全ての計算済み
print(naihouhyouki)
print("====ここから2回目のリスト内包表記===")
print(naihouhyouki)

# ジェネレーター式で書いた場合
generator = (x % 2 == 0 for x in range(100))  # この時点では計算されていない
print(generator)
for is_even in generator:  # このタイミングで計算される
    print(is_even)

print("====ここから2回目のジェネレーター式===")
for is_even_2 in generator:
    print(is_even_2)
