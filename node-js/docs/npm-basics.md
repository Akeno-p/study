# npmの基礎

## Node.jsとは

JavaScriptをブラウザの外（PCやサーバー上）で実行するための環境。
TailwindやReactなどのフロントエンド開発ツールを動かすのに使われる。

---

## npmとは

Node.jsのパッケージマネージャー。Pythonでいう`pip`にあたる。

| Python             | Node.js        |
| ------------------ | -------------- |
| `pip install`      | `npm install`  |
| `requirements.txt` | `package.json` |
| PyPI               | npmレジストリ  |

---

## package.json

npmで管理するパッケージの一覧を記録するファイル。Pythonでいう`requirements.txt`の役割。

`npm init -y`で作成できる。`-y`は全項目をデフォルト値で作成するオプション。

```bash
npm init -y       # package.jsonを作成
npm install tailwindcss  # パッケージを追加（package.jsonに自動記録される）
```

---

## node_modules

`npm install`したパッケージが保存されるディレクトリ。プロジェクトのルートに自動で作られる。

Pythonは`pip install`するとPC全体（グローバル）にインストールされるのがデフォルトだが、npmはプロジェクトの`node_modules`にインストールされるのがデフォルト。つまり最初からプロジェクトごとに分離されている。

---

## npx

プロジェクトの`node_modules`にインストールされているコマンドを実行するツール。

```bash
npx tailwindcss ...
# → このプロジェクトのnode_modulesにあるtailwindcssコマンドを実行
```

Pythonでは仮想環境を`source venv/bin/activate`で有効化してからコマンドを使うが、npmでは`npx`をつけるだけでそのプロジェクトのパッケージを参照してくれる。有効化のような手順は不要。

---

## node_modulesの参照ルール

npmは今いるディレクトリから親ディレクトリへ順番に遡って、最初に見つかった`node_modules`を使う。

```
nofeed-twitter/
├── node_modules/        ← ここにパッケージがある
├── docs/
│   └── design/          ← ここにいても…
└── src/
    └── templates/       ← ここにいても…
```

`docs/design`にいる場合の探索順：

1. `nofeed-twitter/docs/design/node_modules` → ない
2. `nofeed-twitter/docs/node_modules` → ない
3. `nofeed-twitter/node_modules` → ある → これを使う

プロジェクトのどのサブディレクトリにいても、ルートの`node_modules`が参照される。
