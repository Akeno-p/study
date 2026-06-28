# in演算子や部分一致検索の際の注意点


def in_note_1():
    """
    in演算子や部分一致検索に空文字("")を渡すときの注意点

    検索フォーム等で入力を未入力(空文字)を渡すと全てが検索に引っかかる
    """

    # 「空文字はどんな文字列の中にも含まれる」と判定されるためTrue になる
    print("" in "apple")  

    data_list = ["apple", "banana", "orange"]
    search_keyword = ""

    # 悪い例：検索キーワードが空文字だと、全部ヒットしてしまう
    results = [item for item in data_list if search_keyword in item]

    print(results)  # ['apple', 'banana', 'orange']

    # そもそも「空文字ではないこと」を条件にする
    # search_keyword が Truthy（空文字やNoneではない）時だけ検索処理をさせる
    good_results = []
    if search_keyword:  # ← 「空文字ではないこと」を事前チェックする
        good_results = [item for item in data_list if search_keyword in item]
    print(f"良い例: {good_results}")  # []
