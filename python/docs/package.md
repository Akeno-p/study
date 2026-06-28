# パッケージと`__init__.py`について

## パッケージとは

複数のモジュール（`.py` ファイル）を、1つのディレクトリにまとめたもの。

```
users/
    views/
        __init__.py
        mypage.py
        login.py
        logout.py
```

---

## `__init__.py`の役割

そのディレクトリが「パッケージである」ことを示す看板ファイル。

- パッケージが最初に `import` されたときに **1回だけ実行される**（2回目以降はキャッシュされる）。
- 中身は **空でいい**。ファイルが存在すること自体がパッケージの宣言になっている。

```python
# views/__init__.py が空でも動く
from views.mypage import page_open
```

---

## `__init__.py`がなくても動くのか

Python 3.3 以降は、`__init__.py` がなくても `import` は動く。
ただしその場合は **「Namespace Package」** という別モードで処理される。

| 種類               | `__init__.py` | 呼び方            |
| ------------------ | ------------- | ----------------- |
| 通常のパッケージ   | あり          | Regular Package   |
| 名前空間パッケージ | なし          | Namespace Package |

「パッケージにならない」のではなく、「パッケージの種類が変わる」だけ。

---

## なぜ`__init__.py`を置くのか

**ほぼ慣習**

- Python 2 時代は `__init__.py` がないとパッケージとして認識されなかった。その習慣がそのまま残っている。
- `django-admin startapp` 実行時に Django が自動で空の `__init__.py` を作る。
- 周りに `__init__.py` があるから、新しいパッケージにも置く。
- 古いツール・型チェッカ・IDE が `__init__.py` ありを前提にしている場合がある。

技術的には「Namespace Package の落とし穴を避ける」という理由もあるが、個人プロジェクトや単一の Django プロジェクトでそれを踏むことはほぼない。

---

## `__init__.py`の中身を書くメリット

### 再エクスポートによる外向きAPIの整形

```python
# users/views/__init__.py
from .mypage import mypage_open
from .login_and_logout import open_login_and_logout
```

こう書いておくと、外から呼び出すときにサブモジュールを意識しないで済む。

```python
# サブモジュールを直接指定する書き方
from users.views.mypage import mypage_open

# __init__.py で再エクスポートしておけば省略できる
from users.views import mypage_open
```

利点は **「内部実装と外部APIの分離」**。後から `mypage.py` を別の場所に移動しても、`__init__.py` の `import` パスを直すだけで、利用側のコードは1行も変えなくていい。

### パッケージ読み込み時の初期化処理

```python
# __init__.py
import logging
logger = logging.getLogger(__name__)
```

パッケージを最初に `import` したときに1回だけ走らせたい処理（定数定義など）を書ける。

---

## 一旦の理解

> パッケージとは、関連する複数のモジュールを1つのディレクトリにまとめたもの。
> `__init__.py` は「ここはパッケージです」という宣言で、慣習として置く。
> パッケージから何かを `import` すると、サブモジュールより先に `__init__.py` が1回実行される。
