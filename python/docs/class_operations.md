# **call**について。

## 呼び出し方法

`__call__` は、**インスタンスそのものを `()` 付きで呼び出したとき** に発動する特殊メソッド。

```python
class Test:
    def __init__(self):
        self.name = "テスト"
        self.age = 24

    def __call__(self):
        print(f"{self.name}さんは{self.age}歳です")

    def set_info(self):
        self.name = input("ユーザー名を入力してください")
        self.age = input("年齢を入力してください")
```

```python
test = Test()        # __init__ が呼ばれる
test()               # __call__ が呼ばれる → "テストさんは24歳です"
test.set_info()      # set_info が呼ばれる（__call__ は呼ばれない）
```

| 書き方              | 呼ばれるもの |
| ------------------- | ------------ |
| `Test()`            | `__init__`   |
| `test()`            | `__call__`   |
| `test.メソッド名()` | そのメソッド |

ポイント：

- `__call__` は **明示的に `test()` と書いたときだけ** 動く。
- 他のメソッドが芋づる式に動くわけではない。実行されるのは `__call__` の中身だけ。
- メソッド呼び出し（`test.set_info()`）では `__call__` は呼ばれない。

## 一旦の理解

> 「クラスのインスタンスを関数みたいに `()` で呼び出せると便利な場面があるから、Pythonには `__call__` という仕組みが用意されている。
