# any()について

scores = [100, 0, 20, 40]


is_passes = []

for score in scores:
    is_pass = score >= 60  # 60以上が合格
    is_passes.append(is_pass)

print(is_passes)

# anyはイテラブルなものを引数として受け取ることができ、
# 1つでもTrue(truthy)だったらTrueを返す。
if any(is_passes):
    print("彼は合格しました")
else:
    print("彼は不合格でした")

# リスト内包表記やジェネレーター式を引数に渡すこともできる(イテラブルなので)

if any(score >= 60 for score in scores):
    print("彼は合格しました")
else:
    print("彼は不合格でした。")
