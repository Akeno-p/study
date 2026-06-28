# JavaScriptの基本的な知識など

## src について

jsのファイルをhtmlファイル内に読み込ませることができる
書き方は絶対pathを使うか、相対pathを使うか

```js
// 絶対pathの場合
// サーバーの最上位フォルダからのパスを指定する。
// pathの先頭は(/)から始める
<script src="/book/static/js/index.js"></script>

// 相対pathの場合
// 読み込むhtmlファイルからの相対的なパスを指定する
// pathの先頭は(./)から始める
<script src="./static/js/index.js"></script>

```

## typeof　について

jsで値の型を確認する方法は`typeof`という演算子

```js
let num = 10;

// これでstringと表示される
console.log(typeof num);
```
