# 例外処理

def exception_handling_1():
    """
    try:
        実行したい処理
    except 例外の種類:
        例外の場合の処理
    except : #例外の種類を書かない場合全ての例外が対象になる
        例外の場合の処理
    """
    try:
        age = int(input("年齢を入力してください"))
        if age >= 20:
            print("成人です")
        else:
            print("未成人です")
    except ValueError:
        print("入力が数字ではありません")
    except:
        print("その他エラーです")