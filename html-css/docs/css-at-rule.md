# cssのアットルール

アットルールは、`@` から始まるCSSの特別な書き方。

CSS全体に関わる命令を書く時に使う。

```css
@media @import @font-face @keyframes;
```

## ✒️@media

画面幅などの条件に合わせて、CSSを切り替える。

```css
@media (max-width: 600px) {
  body {
    background-color: #333333;
  }
}
```

この場合、画面幅が `600px` 以下の時だけ、`body` の背景色が変わる。

`@media` の中にも、普通のCSSと同じようにセレクタを書く必要がある。

```css
@media (max-width: 600px) {
  .container {
    display: block;
  }
}
```

`@media` は、端末がスマホかPCかを直接判定するものではない。
基本的には、画面幅などの条件に当てはまるかをブラウザが判定する。

```text
画面幅が600px以下
→ 中のCSSを適用する

画面幅が600pxより大きい
→ 中のCSSを適用しない
```

PCでもブラウザの横幅を小さくすれば、条件に当てはまる。

## @mediaの使い所

`@media` は、画面幅に合わせて見た目やレイアウトを調整する時に使う。

```css
.container {
  display: flex;
}

@media (max-width: 600px) {
  .container {
    display: block;
  }
}
```

この場合、通常は横並びで、画面幅が狭い時は縦並びになる。

大規模なWebサービスで、端末ごとにHTMLやUI構造自体を変える場合、`@media` が担当する範囲とは別の話になる。
その場合は、サーバー側、JavaScript、コンポーネントの切り替えなどで制御することが多い。

`@media` は、CSS側で画面幅などの条件に応じて、見た目やレイアウトを調整するために使う。

## ✒️@import

別のCSSファイルを読み込む。

```css
@import url("./reset.css");

body {
  margin: 0;
}
```

この場合、今のCSSファイルから `reset.css` を読み込む。

`@import` は、基本的にCSSファイルの先頭の方に書く。

```css
@import url("./reset.css");
@import url("./base.css");

.box {
  background-color: aqua;
}
```

ただし、CSSファイルの読み込みはHTMLの `link` で書くことも多い。

```html
<link rel="stylesheet" href="../css/reset.css" />
<link rel="stylesheet" href="../css/main.css" />
```

## ✒️@keyframes

アニメーションの動きを定義する。

```css
@keyframes buttonPop {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.08);
  }

  100% {
    transform: scale(1);
  }
}
```

この場合、`buttonPop` という名前で、「元のサイズ→1.08倍→元のサイズ」という動きを定義している。

`0%` がアニメーションの開始、`100%` が終了で、間の地点を `%` で指定する。

`@keyframes` を定義しただけでは動かない。
要素に `animation` で割り当てて、初めて動く。

```css
button {
  animation: buttonPop 0.4s;
}
```

この場合、`button` が `buttonPop` の動きを `0.4s` かけて再生する。

地点が2つだけの時は、`from` と `to` でも書ける。

```css
@keyframes fadeIn {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}
```

`from` が `0%`、`to` が `100%` と同じ意味になる。

## @keyframesの使い所

`@keyframes` は、複数の地点を経由する動きや、繰り返す動きを作る時に使う。

```css
@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

.loading {
  animation: spin 1s linear infinite;
}
```

この場合、`.loading` が回転し続ける。ローディングのスピナーなどでよく使う。

ホバーで色が変わるような、A→Bに1回だけ変化する動きは `transition` で書くことが多い。

```css
button {
  transition: background-color 0.3s;
}
```

繰り返しや複数ステップの動きは `@keyframes`、1回だけの変化は `transition`、というように使い分ける。
