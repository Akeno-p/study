# before after

## ✒️::before

指定した要素の中身の前に、CSSで内容を追加する。

```html
<p class="text-before">test</p>
```

```css
.text-before::before {
  content: "こんにちわ";
}
```

この場合、表示はこうなる。

```text
こんにちわtest
```

`::before` は、HTMLに直接文字を書かずに、CSS側で装飾を追加したい時に使う。

## ✒️::after

指定した要素の中身の後に、CSSで内容を追加する。

```html
<p class="text-after">test</p>
```

```css
.text-after::after {
  content: "こんにちわ";
}
```

この場合、表示はこうなる。

```text
testこんにちわ
```

`::after` は、リンクの後ろに矢印を付けたり、必須項目の後ろに `*` を付けたりする時によく使う。

## ::beforeと::afterの使い所

本文として読ませたい大事なテキストはHTMLに書く。

```html
<p>これは大事な文章です</p>
```

`::before` / `::after` は、意味のある文章を増やすためではなく、見た目の装飾を追加するために使うことが多い。

```css
.midasi::before {
  content: "●";
  color: red;
  margin-right: 8px;
}
```

この場合、`.midasi` クラスを付けた要素の前に、自動で `●` が付く。

```html
<h2 class="midasi">CSSの基本</h2>
```

```text
● CSSの基本
```

## 注意点

`::before` / `::after` は、基本的に `content` がないと表示されない。

```css
.sample::before {
  content: "";
}
```

空の装飾だけ作りたい場合でも、`content: "";` を書く。
