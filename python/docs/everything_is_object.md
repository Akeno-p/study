# Pythonでは数値も関数もクラスもオブジェクトってどういうこと？

整数も、文字列も、リストも、関数も、クラスそのものも、**全部「オブジェクト」というカテゴリーの仲間**。

## 結論

- Pythonの「オブジェクト」は **属性とメソッドを持てる実体** という広い概念
- すべての値は `object` クラスを根っことして派生している
- 違うのは、それぞれに乗っている **追加の能力** だけ
- Pythonでは「クラスそのもの」もオブジェクト（= `type` のインスタンス）。ここがJSとの大きな違い

## 全部に共通する根っこ

```
object（= すべてのオブジェクトの大元）
├── 1, "hello", True    ← 値を保持するだけのシンプルなオブジェクト
├── [1,2,3], {"a":1}    ← 複数の要素をまとめるオブジェクト
├── def func(): ...     ← 「呼び出せる」能力が追加
└── class MyClass: ...  ← 「インスタンスを作れる」能力が追加
```

`type()` で見ると、Pythonの内部での扱いが分かる。

```python
type(1)              # <class 'int'>
type("hello")        # <class 'str'>
type([1, 2, 3])      # <class 'list'>
type(lambda x: x)    # <class 'function'>
type(int)            # <class 'type'>   ← クラスもオブジェクト
```

`isinstance(x, object)` は、どんな値で試しても `True` が返ってくる。

```python
isinstance(1, object)          # True
isinstance("hello", object)    # True
isinstance([1, 2, 3], object)  # True
isinstance(int, object)        # True   ← intクラス自体もobject
```

## ケース① 整数や文字列も「オブジェクト」

「**値を保持するだけのシンプルなオブジェクト**」。
それでも属性（メソッド）を持っており、`.メソッド名()` で操作できる。

```python
num = 5
num.bit_length()      # 3      ← intクラスのメソッド
num.__add__(3)        # 8      ← num + 3 の正体

name = "taro"
name.upper()          # "TARO"
name.startswith("t")  # True
```

`5` という値が単なる「数字」ではなく `int` クラスのインスタンスというオブジェクトだから、こうしてメソッドが呼び出せる。
JSでは数値や文字列はプリミティブで、Pythonとはここが大きく違う。

## ケース② 関数

「**呼び出せる能力（`__call__`）がついたオブジェクト**」。

```python
def test(a=3):
    b = a + 5
    return b
```

属性をのぞくとこんな形。

```python
test {
    __name__:     "test",
    __doc__:      None,
    __defaults__: (3,),           # デフォルト引数
    __code__:     <code object>,  # 中身のバイトコード
    __call__:     <method>,       # 「呼び出せる」の正体
    ...
}
```

- `__call__` を持っているかどうかが「呼び出せる」の判定基準
- `関数名()` の `()` は、**この `__call__` を起動するスイッチ**
- 普通のオブジェクトと同じく、属性を自由に足せる

```python
test.description = "テスト用の関数"
test.author = "Taro"

print(test.description)   # "テスト用の関数"
print(test.__name__)      # "test"  ← 最初から付いている属性
print(test.__defaults__)  # (3,)
```

`callable()` で「呼び出せるオブジェクトかどうか」を判定できる。

```python
callable(test)  # True   ← __call__を持っている
callable(5)     # False  ← intには__call__がない
```

クラスに自分で `__call__` を実装すれば、インスタンスを関数のように呼び出すこともできる（詳しくは [class_operations.md](class_operations.md) を参照）。

## ケース③ リスト

「**順番付きの要素 + リスト用メソッド**」がついたオブジェクト。

```python
arr = ["みかん", "りんご", "ぶどう"]
```

属性をのぞくとこんな形。

```python
arr {
    # 要素は内部的にインデックスで管理
    0: "みかん",
    1: "りんご",
    2: "ぶどう",

    # listクラス側に置かれているメソッド
    __len__:   <method>,   # len(arr)の正体
    __iter__:  <method>,   # for x in arr の正体
    __getitem__: <method>, # arr[0] の正体
    append:    <method>,
    pop:       <method>,
    sort:      <method>,
    ...
}
```

意外なポイント。

- **`len(arr)` は内部的に `arr.__len__()` を呼んでいる**
- **`for x in arr` は内部的に `arr.__iter__()` を呼んでいる**
- **`arr[0]` は内部的に `arr.__getitem__(0)` を呼んでいる**
- **`append`, `pop`, `sort` などのメソッドは `list` クラス側に置かれている**（`list.__dict__` で確認できる）
- **属性の後付けはできない**（ここがJSの配列と違う）

```python
arr.description = "果物リスト"
# AttributeError: 'list' object has no attribute 'description'
```

これは `list` が組み込み型としてC側で固定されていて、自由に属性を生やせないため。
属性を持たせたい場合は、`list` を継承した自作クラスを作るのが一般的。

## Python独自のポイント：クラスもオブジェクト

JSと大きく違うのは、**クラス自身も `type` のインスタンスというオブジェクト** であること。

```python
class Person:
    pass

type(Person)                # <class 'type'>
isinstance(Person, object)  # True

# クラスに属性を後付けできる
Person.species = "human"
print(Person.species)       # "human"

# クラスを変数に入れたり、引数として渡したりできる
def create(cls):
    return cls()

obj = create(Person)        # クラスを関数に渡せる
```

「クラス = インスタンスを作れる能力を持ったオブジェクト」と捉えると、`Person()` という呼び出しが「クラスというオブジェクトの `__call__` を起動して、新しいインスタンスを返している」という挙動として見えてくる。
