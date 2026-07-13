# GitHubコマンドとプルリクエスト（PR）

`gh` コマンド（GitHub公式CLI）と、PRを使った開発フローについて。

---

## ⭐️ GitHub Flow（一番よく使われる開発フロー）

```
main から ブランチを切る
  ↓
作業してコミット
  ↓
push（リモートにブランチを送る）
  ↓
PR を作る
  ↓
（レビュー）
  ↓
merge
  ↓
ブランチを削除
  ↓
main を最新化
```

### コマンドで書くと

```bash
# 1. ブランチを切る（未コミットの変更もそのまま付いてくる）
git switch -c feature/login-screen

# 2. コミット
git add templates/
git commit -m "feat: add login screen template"

# 3. GitHubにpush（初回は -u が必要）
git push -u origin feature/login-screen

# 4. PRを作る
gh pr create

# 5. マージ
gh pr merge --squash --delete-branch

# 6. mainを最新にする
git switch main
git pull
```

---

## ⭐️ gh コマンド（GitHub CLI）

ブラウザを開かずに、ターミナルからGitHubを操作できる公式ツール。

| コマンド         | 説明                         |
| ---------------- | ---------------------------- |
| `gh auth login`  | GitHubにログインする         |
| `gh auth status` | ログインできているか確認する |
| `gh pr create`   | PRを作成する（対話形式）     |
| `gh pr list`     | PRの一覧を表示               |
| `gh pr view`     | PRの内容を表示               |
| `gh pr merge`    | PRをマージする               |
| `gh repo view`   | リポジトリの情報を表示       |

---

## ⭐️ マージ戦略（3種類）

`gh pr merge` でどれを使うか選べる。

| 戦略             | オプション | 何が起きるか                                        |
| ---------------- | ---------- | --------------------------------------------------- |
| Merge commit     | `--merge`  | ブランチの分岐・合流がそのまま履歴に残る            |
| **Squash merge** | `--squash` | ブランチ内の**全コミットを1つに潰して**mainに乗せる |
| Rebase merge     | `--rebase` | 各コミットをmainの先端に付け替える（直線的な履歴）  |

### どれを使うか

学習中・個人開発では **`--squash` が扱いやすい**。

理由：作業中は「wip」「typo修正」みたいな汚いコミットが必ず出る。
squashならそれが**mainに漏れない**。
mainのログが「1機能 = 1コミット」で綺麗に並ぶ。

```bash
gh pr merge --squash --delete-branch
```

`--delete-branch` を付けると、マージ後にブランチも消してくれる。

履歴の形の違いは `git log --graph --oneline` で見比べると分かりやすい。

## ⭐️ PRに何を書くか

**1人開発でもPRの本文は書く。レビュアーがいないなら、未来の自分がレビュアー。**

書くべきは3つ。

| 項目             | 内容                                                         |
| ---------------- | ------------------------------------------------------------ |
| **What**         | 何をしたか                                                   |
| **Why**          | **なぜそうしたか**（設計判断、選ばなかった選択肢）           |
| **How verified** | どう確認したか（「/loginをブラウザで開いて表示を確認」など） |
