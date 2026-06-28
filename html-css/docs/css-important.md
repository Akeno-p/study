# cssの!important

`!important` は、そのCSSの指定を最優先で適用させるための書き方。

```css
p {
  color: red !important;
}
```

値のうしろに `!important` を付ける。

## ✒️何より強いのか

CSSの優先順位は、普段はこの順番で決まる。

```text
1. セレクタの詳細度（id > class > 要素 など）
2. 書かれた順番（あとに書いた方が勝つ）
```

`!important` は、この勝負そのものをスキップして、最優先で適用される。

```css
p {
  color: blue;
}

#main p {
  color: green;
}

p {
  color: red !important;
}
```

この場合、`#main p` の方が詳細度は高いが、`!important` が付いた `red` が勝つ。

## ✒️!important同士の場合

`!important` 同士がぶつかった時は、通常のCSSと同じように、詳細度や書かれた順番で勝負が決まる。

```css
p {
  color: red !important;
}

#main p {
  color: green !important;
}
```

この場合、両方に `!important` が付いているので、詳細度の高い `#main p` の `green` が勝つ。

## @importantの使い所

`!important` は、どうしても他の指定に勝てない時の、最終手段として使う。

```css
.btn {
  color: red !important;
}
```

- 外部ライブラリのCSSを、自分側で上書きしたい時
- どうしても他の指定に勝てない一部分だけ、ピンポイントで効かせたい時

ただし、`!important` は多用しないほうが良いとされている。

```text
!importantを使う
→ 上書きするには、さらに!importantが必要になる
→ どこで何が効いているのか追いにくくなる
```

基本は詳細度や記述順で解決して、`!important` はここぞという場面だけで使うようにする。

## ✒️AIに修正を頼む時の注意

AIは、`!important` を結構使いがちなので注意する。

```text
「なぜかフォントが赤くならない。修正して」
→ !importantを付けて解決してくることが多々ある
```

その場で見た目は直るが、本来は詳細度や記述順で解決できる場面でも `!important` を足してしまうことがある。

修正を頼む時は、`!important` を使わずに直せないか、一度確認するようにする。

