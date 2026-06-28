# gitの設定（config）について

## core.quotepath

日本語のファイル名を `git status` などで**正しく表示する**ための設定。
デフォルトでは日本語がエスケープされて文字化けのように表示される。

```bash
git config --global core.quotepath false
```

`--global` をつけると、すべてのリポジトリに対してこの設定が適用される。
