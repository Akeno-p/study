# リスト内包表記とジェネレーター式の使い分け

> **結果を「保管」したいならリスト内包表記、「通り過ぎる」だけならジェネレーター式**

CPU負荷はほぼ同じ。違いが出るのは「メモリ消費」と「途中で打ち切る場合」の2点。

---

## 構文の違いは `[]` か `()` か

```python
scores = [100, 10, 20, 30, 50]

# リスト内包表記
list_comp = [score >= 60 for score in scores]

# ジェネレーター式
gen_exp = (score >= 60 for score in scores)
```

見た目はカッコの違いだけ。

---

## 中身の違い

```python
print(list_comp)
# → [True, False, False, False, False]   ← 計算結果

print(gen_exp)
# → <generator object <genexpr> at 0x...> ← まだ計算されてない
```

|                | リスト内包表記               | ジェネレーター式                   |
| -------------- | ---------------------------- | ---------------------------------- |
| 変数に入るもの | **計算済みの結果**（リスト） | **計算する手順**（ジェネレーター） |
| 計算タイミング | 代入した瞬間に全部           | 取り出すたびに1個ずつ              |

---

## CPU負荷について

「ジェネレーター式の方が常に軽い」わけではない

全要素を処理するなら、計算回数は同じ。
むしろジェネレーター式は `yield` のオーバーヘッドがあるので、わずかに遅いこともあるらしい。

```python
# どちらも比較計算は5回走る → CPU負荷は実質同じ
[x > 60 for x in scores]
(x > 60 for x in scores)
```

---

## ジェネレーター式が本当に効く2つの場面

### ① 途中で処理を抜ける

`any` / `all` / `next` / `break` のように最後まで見ない処理では、ジェネレーター式が良い

```python
# 1個でもTrueが出たら即終了（残りは計算されない）
any(x > 60 for x in scores)

# 最初に見つかったものだけ取得
next(x for x in scores if x > 60)

# breakで抜ける場合も同様
for x in (compute(i) for i in huge_list):
    if condition(x):
        break  # ここまでしか計算されない
```

### ② 巨大データのメモリ節約

CPU負荷は同じでも、メモリ消費はまったく違う。

```python
# リスト内包表記：1000万個を全部メモリに保持
big_list = [x * 2 for x in range(10000000)]

# ジェネレーター式：1個ずつ作って捨てる
big_gen = (x * 2 for x in range(10000000))
```

---

## その他の違い

### 再利用できるか

```python
# リスト内包表記：何度でも使える
naihou = [x*2 for x in [1, 2, 3]]
print(list(naihou))  # [2, 4, 6]
print(list(naihou))  # [2, 4, 6]  ← OK

# ジェネレーター式：一度きり
gen = (x*2 for x in [1, 2, 3])
print(list(gen))  # [2, 4, 6]
print(list(gen))  # []  ← 中身が空になる
```