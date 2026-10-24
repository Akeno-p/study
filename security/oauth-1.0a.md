# OAuth 1.0a

OAuth の旧規格。Google・GitHub・Slack などは OAuth 2.0 のみで、X（旧Twitter）が後方互換のために残している程度。

## 署名する理由

OAuth 1.0a が作られた2007年頃は、HTTP（暗号化なし）が当たり前だった。トークンをそのまま送ると盗聴されるので、秘密の値は送らず、「秘密を知っている」ことだけを署名で示す。

そのため鍵が2組4つある。

| OAuth 1.0a          | OAuth 2.0 での名前 |
| ------------------- | ------------------ |
| Consumer Key        | Client ID          |
| Consumer Secret     | Client Secret      |
| Access Token        | Access Token       |
| Access Token Secret | なし               |

X の管理画面では、Consumer Key / Consumer Secret が "API Key / API Secret" と表記されている。

## 署名の手順

リクエストを送るたびに、ライブラリが裏で行う。

1. リクエスト内容（HTTPメソッド、URL、パラメータ、nonce、timestamp）を、決まった手順で1本の文字列にまとめる（signature base string）
2. `Consumer Secret` + `&` + `Access Token Secret` をつなげて署名鍵を作る
3. その鍵で base string を HMAC-SHA1 にかける → 署名
4. 次の内容を送る。Secret は含まれない

```
Authorization: OAuth
  oauth_consumer_key="...",     ← 名乗り（アプリ）
  oauth_token="...",            ← 名乗り（ユーザー）
  oauth_signature="...",        ← 証明
  oauth_nonce="...",
  oauth_timestamp="...",
  oauth_signature_method="HMAC-SHA1"
```

## サーバー側の検証

サーバーは `oauth_consumer_key` と `oauth_token` から、自分が発行した Secret を DB で引いて同じ計算をする。結果が届いた署名と一致すれば、相手も同じ Secret を持っているので本物と分かる。

## Secret が2つとも必要な理由

署名鍵は2つの Secret をつなげたものなので、片方だけ盗んでも正しい署名は作れない。これで「このアプリが、このユーザーの許可を得てリクエストしている」ことを示せる。

## リプレイ攻撃への対策

盗聴したリクエストを丸ごと再送信されると、署名は正しいまま通ってしまう（リプレイ攻撃）。

そこで毎回、nonce（使い捨てのランダム文字列）と timestamp を混ぜて署名する。サーバーは使用済みの nonce や、古すぎる timestamp を弾く。

## OAuth 2.0 で署名がなくなった理由

2012年頃には HTTPS が普及していた。通信路が暗号化されるなら署名は要らないと判断され、OAuth 2.0 では署名が廃止された。2.0 ではアクセストークンを持っていること自体が証明になるので、Access Token Secret もなくなった。
