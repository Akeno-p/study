# Margin Collapse

上下の `margin` は、条件がそろうと親の外側に出ることがある。

これを `margin collapse`、日本語では `marginの相殺` という。

## 例

```html
<header>
  <h1>Title</h1>
</header>
```

`h1` にはブラウザのデフォルトで上下の `margin` がある。

親の `header` に `padding` や `border` がない場合、`h1` の上下marginが `header` の外側に出ることがある。

その結果、`header` の高さには `h1` のmargin分が含まれない。

```text
h1のmargin
header
  h1本体
h1のmargin
```

## paddingで止まる理由

`padding` がない場合、親の端と子のmarginが直接接する。

```text
headerの端
h1のmargin
h1本体
```

このとき、margin相殺が起きる。

`padding` がある場合、親の端と子のmarginの間に `padding` が入る。

```text
headerの端
padding
h1のmargin
h1本体
```

親の端と子のmarginが直接接しないので、margin相殺が起きない。

## 対策

今回のように `h1` のデフォルトmarginが原因なら、素直に消す。

```css
h1 {
  margin: 0;
}
```

余白が必要なら、親側に `padding` を指定する。

```css
header {
  padding: 20px;
}
```

ただし、margin相殺を止めるためだけに `padding` を入れるのは分かりにくいので相殺を止めるのが目的なら`margin:0;`を使用しよう。
