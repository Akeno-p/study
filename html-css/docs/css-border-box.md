# box-sizingについて

要素の幅や高さを計算するときに、`padding` と `border` を含めるかどうかを決める。

## content-box

`box-sizing` の初期値。

```css
div {
  width: 500px;
  padding: 100px;
}
```

この場合、`width: 500px;` は中身部分の幅だけを指定している。

そのため、左右の `padding` が追加されて、実際の横幅は大きくなる。

```text
中身の幅 500px
左padding 100px
右padding 100px

実際の横幅 700px
```

`padding` は要素の内側の余白。
ただし、初期状態では `width` の中に収まるのではなく、`width` に追加される。

## border-box

`padding` と `border` を、指定した `width` や `height` の中に含める。

```css
div {
  box-sizing: border-box;
  width: 500px;
  padding: 100px;
}
```

この場合、実際の横幅は `500px` のままになる。

```text
全体の幅 500px
その中に 左padding 100px + 右padding 100px も含める
```

そのため、中身が使える幅は小さくなる。

```text
500px - 100px - 100px = 300px
```

## marginの扱い

`box-sizing: border-box;` に含まれるのは、`padding` と `border`。
`margin` は含まれない。

## paddingが大きすぎる場合

`border-box` でも、どんな `padding` でも必ず指定した `width` に収まるわけではない。

```css
div {
  box-sizing: border-box;
  width: 100px;
  padding: 80px;
}
```

この場合、左右の `padding` だけで `160px` になる。
`width: 100px;` に収まらないので、最低限 `padding` が入る幅までは広がる。

## 実務でよく使う形

実務では、最初に全体へ指定することが多い。

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

こうすると、`padding` や `border` を付けても、指定した幅からはみ出しにくくなる。

特に、`width: 100%;` のフォームやカードなどで扱いやすい。

```css
input {
  width: 100%;
  padding: 12px;
}
```

`box-sizing` なしだと、`width: 100%;` に `padding` が追加されて親からはみ出すことがある。

`border-box` にしておくと、`padding` 込みで親の幅に収まりやすくなる。

## まとめ

```text
content-box:
指定したwidthにpaddingとborderが追加される

border-box:
指定したwidthの中にpaddingとborderを含める
```

`box-sizing: border-box;` は、レイアウトの幅を計算しやすくするために使う。
