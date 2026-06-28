# pythonの命名規則

## 命名規則について

### 変数名・関数名・メソッド名・ファイル名

- 小文字 + \_

```python
user_name = ~~~
address = ~~~
```

### 定数名

※ 定数 : 一度設定したら後から変更しない変数

- 大文字 + \_

```python
MATER_CODE = ~~~
FILE_NAME = ~~~
```

### クラス名

- 単語の先頭だけ大文字

```python
UserClass
CommonClass
```

---

## Bool値が入る変数名

どっちのときが`True`でどっちのときが`False`なのかわかるようにするために
`is_〇〇`,`has_〇〇`,`can_〇〇`,という命名にする。

```python
is_student = True # 学生かどうか?
can_login = True # ログイン可能かどうか？
has_pc = True # PCを持っているかどうか?
```
