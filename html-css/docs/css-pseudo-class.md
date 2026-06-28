# cssの擬似クラス

擬似クラスは、要素の状態や条件に合わせてCSSを当てる書き方。

`:` を使って書く。

```css
セレクタ:擬似クラス {
  プロパティ: 値;
}
```

## ✒️:hover

マウスが乗っている時だけCSSを適用する。

```css
button:hover {
  background-color: aqua;
}
```

この場合、`button` にマウスが乗った時だけ背景色が変わる。

## ✒️:active

クリックしている間だけCSSを適用する。

```css
button:active {
  background-color: tomato;
}
```

この場合、`button` を押している間だけ背景色が変わる。

## ✒️:focus

要素が選択されている時にCSSを適用する。

```css
input:focus {
  border: 1px solid brown;
  outline: none;
}
```

この場合、`input` が選択されている時だけ枠線が変わる。

## :focusが使える要素

`:focus` は `input` 専用ではない。
フォーカスできる要素に使える。

```css
textarea:focus {
  border-color: blue;
}

button:focus {
  outline: 2px solid red;
}

a:focus {
  color: red;
}
```
