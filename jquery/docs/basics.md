# jQuery 基本メモ

## 書き始め方

jQueryのコードはHTMLの読み込みが終わってから実行する必要がある。
そのために以下のように書く。

```js
$(document).ready(function () {
  // ここにjQueryのコードを書く
});
```

短縮形もある。やっていることは同じ。

```js
$(function () {
  // ここにjQueryのコードを書く
});
```

## jQueryオブジェクトを変数に入れる

何回も使うjQueryオブジェクトは変数に入れておくと便利。

```js
// 毎回 $("h1") を書かなくて済む
const $h1 = $("h1");

$h1.css("color", "red");
$h1.text("Hello!");
```

変数名の先頭に `$` をつけるのが慣習。
