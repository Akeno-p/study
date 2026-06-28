## cliコマンドについて

## claude --name "session-name"

session-nameの値でセッションが起動する

## claude --resume

過去の会話履歴から再開できる

## claude --worktree "値"

新しいworktree内でセッションを開く
worktreeはリポジトリルートの`.claude/worktrees/`の中にできる
ブランチ名はworktree-値になる

作成されたworktreeはセッション終了時に変更がなければ自動で削除され
変更がある場合は残すか消すか聞かれる。
