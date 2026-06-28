他人が最短時間で理解できるコードを書こう。

▼ djangoの例

```python
# あまり良くない例：条件が1行に詰め込まれていて、何を判定しているのかパッと見でわからない
if user.age >= 20 and (datetime.now() - user.date_joined).days < 365 and user.occupation == "engineer":
    send_campaign_email(user)

# いい例：条件を分けて書くことで、何で弾かれるのかが明確
if user.age < 20:
    print("20歳未満のため対象外です")
elif (datetime.now() - user.date_joined).days >= 365:
    print("登録から1年以上経過しているため対象外です")
elif user.occupation != "engineer":
    print("エンジニア以外は対象外です")
else:
    send_campaign_email(user)
```

自分が書いたんだから問題ない。と思っても将来の自分はほぼ他人みたいなものなので自分のためにもわかりやすく書こう。

## AI時代だからこそリーダブルコードが大事

これからはAIがコードを書いて、人間がレビューする時代になっていく。
AIが書いたコードは動くけど、読みにくいことも多い。自分で書いていないぶん記憶への定着も薄い。

だからこそ、AIが出力したコードに対しても「そこはわかりづらいから普通にif文で書いて」みたいに指示できる力が大事。
難しい書き方のまま通してしまうと、将来自分で読まなきゃいけなくなった時に地獄になる。

「動けばいい」ではなく「読めるかどうか」を基準にレビューしよう。

## 名前は思ったよりもずっと大事

変数名や関数名、クラス名は「なんとなく」でつけがち。でも名前が曖昧だと、読む人はそこで立ち止まって考えることになる。

```python
# あまり良くない例
def get_data():
    ...
```

get って何？ どこから取ってくるの？インターネット？ローカル？ そもそも data って何のデータ？
これだと名前だけでは何も伝わらない。

```python
# いい例
def fetch_daily_progress_report():
    ...
```

これなら「外部から取得する」「日次の」「進捗レポート」と、名前だけで何をする関数かわかる。

「コメントで補足すればいいや」という考えはやめよう。
コメントは古くなったり消されたりするけど、名前はコードがある限りずっと残る。
名前そのものが説明になるようにつけよう。

## 見た目の美しさ

見た目が綺麗、整っていると見やすいので見た目を整えたほうがいい。

だけど、インデントや改行の一貫性といった「見た目の整え」は、PrettierやBlackなどのフォーマッターを使えばほぼ自動で解決できる。
ここは今の時代、ツールに任せてしまって問題ない。

ただし、**コードの並び順**はフォーマッターがやってくれないので、ここは自分で意識する必要がある。

```python
# あまり良くない例：順番がバラバラで全体像がつかみにくい
def update_user():
    ...

MAX_RETRY = 3

def get_user():
    ...

BASE_URL = "https://example.com"

def delete_user():
    ...

# いい例：種類ごとにまとめ、処理の流れに沿った順番にする
BASE_URL = "https://example.com"
MAX_RETRY = 3

def get_user():
    ...

def update_user():
    ...

def delete_user():
    ...
```

意識するポイント：

- 定数 → 変数 → 関数のように、種類ごとにまとめる
- 関連する関数は近くに置く
- 処理の流れや重要度に沿った順番で並べる

並び順が整っているだけで、ファイルを開いたときに「このコードは何をしているか」がすぐ伝わる。

## コメントは「見てわかること」には書かない

```python
# あまり良くない例：見ればわかることをコメントしている
# ユーザー登録の関数を定義
def register_user():
    ...
```

関数名を読めばわかることをわざわざコメントに書いても、ノイズが増えるだけ。

### コメントを書くべきとき

**1. コードを見ただけではわからないこと・読んだ人が疑問に思いそうなこと**

```python
# 外部APIの仕様上、リトライは最大3回までしか許容されない
MAX_RETRY = 3
```

なぜその値なのか、なぜその書き方なのか、という「Why」はコードからは読み取れない。

**2. 複雑な処理の要約**

```python
# この関数は会員登録や会員情報編集時のバリデーションに使用している
def validate_user_input(data):
    ...
```

低レベルな処理が続くコードに対して「結局これは何をしているのか」「どこで使われているのか」を一言で書いておくと、読む人が全体像をつかみやすくなる。

## 制御フローを読みやすくする

### 条件式は「日本語にして自然な順番」で書く

条件式の左辺には「調べたい対象」、右辺には「比較する基準値」を置くと読みやすい。
判断のコツは、「左辺が右辺なら」と日本語に置き換えてみて自然かどうか。

```python
# 読みやすい：「年齢が20以上なら」と自然に読める
if age >= 20:
    ...

# 読みにくい：「20が年齢以下なら」…意味がすぐ入ってこない
if 20 <= age:
    ...
```

左辺＝調べたい対象、右辺＝基準値。これを意識するだけで条件式がぐっと読みやすくなる。

### if/elseの順番

**関心（影響）が大きい条件を先に書く**

読む人がまず知りたいのは「どういうときにOKなのか」「メインの処理は何か」ということ。
重要な条件を先に持ってくることで、コードの意図がすぐ伝わる。

**条件はなるべく肯定形で書く**

```python
# わかりやすい：肯定形で書いている
if age >= 20:
    print("20歳以上なのでOKです")
else:
    print("20歳未満のため対象外です")

# わかりづらい：否定形で書いている
if not age >= 20:
    print("20歳以上ではないのでNGです")
else:
    print("それ以外の人はOKです")
```

否定形の条件は、読む人の頭の中で「notってことは…つまり20歳未満？」と一度変換が必要になる。
肯定形で書けば、条件がそのまま意味として頭に入ってくる。

## 説明変数

式を変数に入れて名前をつけることで、「この式は何を判定しているのか」を読む人にすぐ伝えるテクニック。

```python
# 説明変数なし：読む人が式の意味を一つずつ解読する必要がある
if user.age >= 20 and user.country == "JP" and user.is_verified:
    serve_alcohol()

# 説明変数あり：変数名だけで何を判定しているかわかる
is_adult = user.age >= 20
is_japanese = user.country == "JP"
is_verified = user.is_verified

if is_adult and is_japanese and is_verified:
    serve_alcohol()
```

動作は全く同じ。違いは「読む時の脳の負担」。

- 直接書く → if文を読みながら「この式は何を意味してるんだ？」と**式の意味を解読する作業**が発生する
- 説明変数 → 変数名で「成人かどうかね」とわかるから、**処理の流れだけ追えばいい**

### 一回しか使わなくても説明変数に入れる価値はある

説明変数の目的は「再利用」ではなく「読みやすさ」。

たとえ一回しか使わない条件でも、式が複雑なら変数に入れることで読む人の解読コストを減らせる。
「何回使うか」ではなく「読む人の脳の負担が減るかどうか」で判断しよう。

## 関数はひとつのことだけやる

関数に複数の目的を詰め込まない。「バリデーション」「DB保存」「メール送信」のように目的が違うものは関数を分ける。

```python
# よくない例：1つの関数にバリデーション・DB保存・メール送信が全部入っている
def register_user(data):
    if not data.get("email"):
        raise ValueError("メールアドレスは必須です")
    if not data.get("password"):
        raise ValueError("パスワードは必須です")
    if len(data["password"]) < 8:
        raise ValueError("パスワードは8文字以上必要です")

    user = User.objects.create(
        email=data["email"],
        password=hash_password(data["password"]),
    )

    send_welcome_email(user.email)
    return user

# いい例：目的ごとに関数を分ける
def validate_registration_data(data):
    if not data.get("email"):
        raise ValueError("メールアドレスは必須です")
    if not data.get("password"):
        raise ValueError("パスワードは必須です")
    if len(data["password"]) < 8:
        raise ValueError("パスワードは8文字以上必要です")

def create_user(data):
    return User.objects.create(
        email=data["email"],
        password=hash_password(data["password"]),
    )

def register_user(data):
    validate_registration_data(data)
    user = create_user(data)
    send_welcome_email(user.email)
    return user
```

### 分ける判断基準

「この関数は何をする関数？」と聞かれた時に一言で答えられるかどうか。

- 「入力値をチェックする関数」→ OK
- 「入力値をチェックして、DBに保存して、メールを送る関数」→ 「と」で繋がってる = 分けるサイン

ただし同じ目的の中で細かく分けすぎるのはやりすぎ。
「emailのバリデーション」「passwordのバリデーション」「password長さのバリデーション」は全部「入力値のバリデーション」という同じ目的なので、1つの関数にまとまっていた方が読みやすい。

### なぜ分けると読みやすいのか

上から順に読めるなら全部入りでもよくない？と思うかもしれないが、実際の開発では全体を読むことはほぼない。
何千・何万行のコードの中から「該当部分だけ変える」のが基本。

- バリデーションのルールを変えたい → `validate_registration_data` だけ見ればいい
- メール送信をやめたい → `register_user` の中の1行を消すだけ
- バグを探したい → 原因がありそうな関数だけ読めばいい

全部入りだと「バリデーションを変えたいだけなのに、DB保存やメール送信のコードまで読まされる」ことになる。
関数が分かれていれば、関係ない処理は目に入らないし、依存関係がないことも関数の構造から保証される。

### 分けた関数にはデータの構造を明示する

関数を分けると「この関数にはどういうデータを渡せばいいの？」が見えなくなりがち。
型ヒントやクラスでデータの構造を明示してあげると、関数の中身を読まなくても使い方がわかる。

```python
# 型ヒントで引数と戻り値の構造を明示する
class RegistrationData:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

def validate_registration_data(data: RegistrationData) -> None:
    ...

def create_user(data: RegistrationData) -> User:
    ...
```

DjangoならSerializerやFormがこの役割を果たしている。

```python
# Serializerそのものが「dataの構造はこうだよ」という説明になっている
class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
```

