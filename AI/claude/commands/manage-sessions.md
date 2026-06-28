# セッション管理系のコマンドたち

## /branch

セッションの内容をコピーして新しいセッションを作成することことができる。
引数で名前を指定してあげる

```test
/branch new-session-name
```

## /rename

セッションに名前をつけることができる。
名前を指定しないと、どれがどのセッションかわけわからなくなるのでつけておいた方がいい。

## /resume

セッションを切り替えることができるコマンド

## /rewind

セッション内の会話を巻き戻したりできるコマンド
escキー2回でも同じことができる

巻き戻す際に

1. Restore code and conversation：　コードと会話を復元する
2. Restore conversation：　会話を復元する
3. Restore code：　コードを復元する
4. Summarize from here：　選択した場所以降を圧縮(/compact)する
5. Summarize up to here：　選択した場所以前を圧縮(/compact)する

※ 4と5はセッションの操作というよりcontextの操作

### summarize　と　compactの違い

特定の範囲を指定したい場合はsummarizeを使う。
