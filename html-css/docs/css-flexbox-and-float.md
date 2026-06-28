# Flexboxとfloatの違い

## `display: flex;` とは

`display: flex;` は、指定した要素をFlexboxの親要素にするCSS

```css
ul {
  display: flex;
}
```

この場合、`ul` の直接の子要素である `li` がFlexboxで並べられる対象になる。

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
```

つまり、`display: flex;` は「その要素自身を横並びにする」というより、親要素に指定して「子要素の並び方をコントロールできる状態にする」やつ。

Flexboxは初期状態で横並びになっている。

そのため、子要素は左から右の横並びになる。

なので横並びにするだけなら、`display: flex;`をつけるだけで終わる

```css
ul {
  display: flex;
}
```

## `float: left;` でも横並びにはできる

`float: left;` を使っても、要素を横並びにできる。

```css
li {
  float: left;
}
```

ただし、`float` は本来、画像などの横に文章を回り込ませるための機能らしい。
なのでただ横並びにしたいだけなら`display: flex;`の方が自然

## 横並びレイアウトではFlexboxがよく使われる理由

現在は、メニューやカードなどを横並びにする場合、`float` より `display: flex;` がよく使われる。

理由は、Flexboxの方がレイアウト用として扱いやすいかららしい。

- 親要素の高さが崩れにくい
- 要素同士の間隔を `gap` で指定できる
- 中央寄せや右寄せが簡単
- 縦並びと横並びを切り替えやすい
- CSSを読んだときに、レイアウト目的だと分かりやすい

例えば、要素同士の間隔を空ける場合はこう書ける。

```css
ul {
  display: flex;
  gap: 20px;
}
```

## まとめ

- `display: flex;` は親要素に指定する
- 指定された親要素の直接の子要素がFlexboxで並べられる
- Flexboxのデフォルトは横並び
- 横並びだけなら `display: flex;` だけでよいことが多い
- `float: left;` でも横並びにはできる
- 横並びレイアウトには、現在はFlexboxの方が自然で扱いやすい
