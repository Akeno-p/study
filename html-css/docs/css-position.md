# positionについて

要素の位置を指定するためのプロパティ。

`position` を指定した要素は、`top`、`right`、`bottom`、`left` で位置を調整できる。

```css
.box {
  position: relative;
  top: 20px;
  left: 20px;
}
```

## relative

本来の位置を基準にして、見た目だけ動かす。

```css
.position-relative {
  position: relative;
  top: 20px;
  left: 20px;
}
```

この場合、本来の位置から下に `20px`、右に `20px` 動く。

ただし、元の場所は残ったままになる。
そのため、他の要素と重なることがある。

```text
元の場所は確保されたまま
見た目だけ動く
```

## absolute

position指定済みの親を基準にして、位置を指定する。

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 30px;
  left: 100px;
}
```

この場合、`.child` は `.parent` を基準にして配置される。

```text
親の上端から30px
親の左端から100px
```

`absolute` は、自分より上の階層にある `position` 指定済みの親を探す。
一番近い親を基準にする。

よく使う形は、親に `relative`、子に `absolute`。

```css
.parent {
  position: relative;
}

.child {
  position: absolute;
}
```

親の `relative` は、親自身を動かすためではなく、子の `absolute` の基準にするために使うことが多い。

## absoluteの基準

`top`、`right`、`bottom`、`left` のどれを使うかで、見る場所が変わる。

```css
.child {
  position: absolute;
  top: 0;
  left: 0;
}
```

この場合、基準になる親の左上に配置される。

```text
top: 親の上端からの距離
right: 親の右端からの距離
bottom: 親の下端からの距離
left: 親の左端からの距離
```

親に `border` がある場合、基準は親の `border` の内側になる。

## fixed

画面を基準にして、位置を固定する。

```css
.position-fixed {
  position: fixed;
  top: 300px;
  left: 300px;
}
```

スクロールしても、常に画面上の同じ場所に表示される。

固定ヘッダーや、右下に固定するボタンなどで使う。

## sticky

普段は通常の位置にあり、スクロールして指定位置に来たら固定される。

```css
.position-sticky {
  position: sticky;
  top: 30px;
}
```

この場合、スクロールして画面上から `30px` の位置に来ると、そこに張り付く。

## まとめ

```text
relative:
本来の位置を基準に、見た目だけ動かす

absolute:
position指定済みの親を基準に、位置を指定する

fixed:
画面を基準に、位置を固定する

sticky:
途中までは普通に配置され、指定位置まで来たら固定される
```
