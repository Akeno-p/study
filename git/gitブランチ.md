# gitのブランチ名

ブランチ名の命名規則（`feature/` など）と、`/` の正体について。

---

## ⭐️ ブランチ名の `/` は階層ではない

`feature/login-screen` は、**`/` を含んだ1つの文字列**でしかない。

「`feature` の中に `login-screen` ブランチがある」という階層構造**ではない**。
そもそも `feature` という親ブランチは**存在しない**。

---

## ⭐️ `/` はわかりやすくするためのもの。(ほぼ慣習)

コミットメッセージの `feat:` `chore:` と**まったく同じ発想**。
人間が読んで分かるように先頭につけているだけで、**Gitは何の特別扱いもしていない**。
ただ、みんな`/`で区切るので一部ツールではツリー表示してくれたりする。

| prefix           | 意味                   |
| ---------------- | ---------------------- |
| `feature/`       | 新機能                 |
| `fix/` `bugfix/` | バグ修正               |
| `hotfix/`        | 本番の緊急修正         |
| `refactor/`      | 挙動を変えない整理     |
| `docs/`          | ドキュメントのみ       |
| `chore/`         | 雑務（設定・依存更新） |

---

## 🔧 ディレクトリは掘られる。でも「だから何」という話は一切ない

ブランチの実体は `.git/refs/heads/<名前>` という**ファイル**。
中身は**コミットハッシュが1行書いてあるだけ**（→ 「ブランチはコミットへのポインタ」）。

ファイルとして保存する以上、名前に `/` があれば**本当にディレクトリが掘られる**。

```
.git/refs/heads/
├── feature/            ← 本物のディレクトリができる
│   └── login-screen
└── main
```

**ただしこれは、Gitの意味論ではなく「保存方法の副作用」でしかない。**

### 証拠：ディレクトリは消える。それでもブランチは動く

Gitはブランチを2通りの方法で保存する。

| 方式            | 保存場所                                          |
| --------------- | ------------------------------------------------- |
| **loose refs**  | `.git/refs/heads/<名前>`（1ブランチ = 1ファイル） |
| **packed refs** | `.git/packed-refs`（全ブランチを1ファイルに集約） |

Gitは最適化のタイミングで、勝手に後者へ切り替える（`git pack-refs` / `git gc`）。
すると **`refs/heads/` のディレクトリは跡形もなく消える**。

```
# .git/packed-refs の中身
98f08db...  refs/heads/feature/login-screen
98f08db...  refs/heads/fix/typo
98f08db...  refs/heads/main
```

---

## 🔧 注意点

`feature/login-screen` が存在すると、**`feature` という名前のブランチは作れなくなる**。

```
$ git branch feature
fatal: cannot lock ref 'refs/heads/feature': 'refs/heads/feature/login-screen' exists;
       cannot create 'refs/heads/feature'
```

ディレクトリと同名のファイルは作れない、というOSの制約が、そのまま仕様に漏れ出している。
