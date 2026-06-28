# cssの色々なプロパティ

## ✒️background-image

背景画像を指定する。

```css
.footer {
  background-image: url("../images/test背景.png");
}
```

画像のパスは `url()` の中に書く。

### 背景を画像にする際によく使用するプロパティ

| プロパティ            | よく使う値  | 意味                                       |
| --------------------- | ----------- | ------------------------------------------ |
| `background-repeat`   | `no-repeat` | 背景画像を繰り返さない                     |
| `background-size`     | `cover`     | 要素全体を埋める。画像が切れることがある   |
| `background-size`     | `contain`   | 画像全体を表示する。余白ができることがある |
| `background-position` | `center`    | 背景画像を中央に表示する                   |

### 背景画像でよく使う形

```css
.footer {
  background-image: url("../images/test背景.png");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
```

## ✒️opacity

不透明度を指定する
値は、0.0 ~ 1.0 までで不透明度を指定する。

```css
/* 70%表示されて30%透明になる */
.footer p {
  opacity: 0.7;
}
```

`opacity` は指定した要素全体に効く。
背景、文字、画像、子要素などもまとめて透明になる。

```css
.opacity-sample {
  background-color: aqua;
  opacity: 0.5;
}
```

この場合、背景だけでなく中の文字も半透明になる。
子要素に `opacity: 1;` を指定しても、親要素の透明度を上書きして完全に不透明には戻せない。

## ✒️rgba

色に透明度をつける。
基本的に、背景色や文字色などの透明度をいじりたい場合は `opacity` より `rgba()` を使う。

```css
/* 背景色だけを50%透明にする */
.opacity-sample {
  background-color: rgba(0, 255, 255, 0.5);
}
```

`rgba()` は、赤、緑、青、透明度の順番で指定する。

```css
rgba(赤, 緑, 青, 透明度)
```

透明度は `opacity` と同じで、0.0 ~ 1.0 で指定する。

文字色に透明度をつけたい場合は `color` に指定する。

```css
.opacity-sample {
  color: rgba(0, 0, 0, 0.5);
}
```

## ✒️letter-spacing

文字の間を指定する

```css
/* 10px分隙間が開く */
.footer p {
  letter-spacing: 10px;
}
```

## ✒️:hover

マウスが乗っている時だけCSSを適用する。

```css
/* h2にマウスが乗った時だけ文字色が変わる */
.h2-hover:hover {
  color: aqua;
}
```

## ✒️transition

変化にかかる時間を指定する。

```css
/* 文字色が0.3秒かけて変化する */
h2 {
  color: blueviolet;
  transition: color 0.3s;
}

.h2-hover:hover {
  color: aqua;
}
```

## ✒️line-height

行の高さを指定する。
文字の上下の余白を調整したい時に使う。

```css
/* 行の高さを100pxにする */
.line-height {
  line-height: 100px;
}
```

`line-height` を大きくすると、行と行の間が広くなる。
指定した高さの中央に配置される。

## ✒️display: block

要素をブロック表示にする。
ブロック表示の要素は、基本的に縦に並ぶ。
display: block; は、指定した要素自身をブロック表示にするので親に書くのではない

```css
.block-sample {
  display: block;
}
```

`width` を指定していない場合は、親要素の横幅いっぱいに広がる。

```css
.block-sample {
  display: block;
  width: 100px;
}
```

`width` を指定した場合は、その幅になる。
ただし、横にスペースが余っていても、次の要素は下に表示される。

## ✒️max-width

これ以上は大きくならない、という上限を決める。

```css
.container {
  max-width: 960px;
}
```

960pxより大きくはならない。
このmaxの値でuiを調整するというよりはuiが崩れないための防波堤的な役割

## ✒️min-width

これ以下は小さくならない、という下限を決める。

```css
.container {
  min-width: 320px;
}
```

320pxより小さくはならない。
このminの値でuiを調整するというよりはuiが崩れないための防波堤的な役割
