# Gridについて
列の幅を指定してマスみたいにして使えるやつ。

## display: grid;

- まずはこれを使って、子要素をグリッドで配置できる状態にする

## grid-template-columns:

列の作り方を決める

```css
grid-template-columns: repeat(3, 1fr); /* 3列にする */
grid-template-columns: 1fr 1fr 1fr; /* repeat(3, 1fr) と同じ意味 */
grid-template-columns: 2fr 1fr 1fr; /* 2:1:1 の幅で3列にする */
```

## grid-template-rows:

行の高さを決める

```css
grid-template-rows: 100px 200px; /* 1行目を100px、2行目を200pxにする */
grid-template-rows: 1fr 2fr; /* 親の高さを1:2で分ける */
```

## repeat():

同じ指定を繰り返す書き方

```css
repeat(3, 1fr); /* 1frを3回繰り返す */
```

## fr:

余っている幅を分ける単位

```css
grid-template-columns: 1fr 1fr 1fr; /* 親の幅を3等分する */
grid-template-columns: 2fr 1fr 1fr; /* 親の幅を2:1:1で分ける */
```

## gap:

コンテンツ同士の隙間をどれくらい空けるか？の話
※ paddingでもmarginでもなく、並んでいる子要素同士の間にできる隙間

```css
gap: 16px; /* 子要素同士の隙間を16px空ける */
```

## 行について

列数を指定しておけば、子要素の数に応じて行は自動で増える

```css
grid-template-columns: repeat(
  3,
  1fr
); /* 3列。子要素が増えたら自動で次の行に並ぶ */
```

## 中央寄せについて

### 親(コンテナ)側で全部まとめて中央寄せ

コンテナに指定するパターン。全部のセルの中身がまとめて中央に寄る。

- 横方向の中央 → `justify-items: center;`
- 縦方向の中央 → `align-items: center;`
- 両方まとめて → `place-items: center;` (上2つのショートハンド)

```css
.about-content {
  display: grid;
  place-items: center; /* 全セルの中身を縦横中央に */
}
```

### 子(個別の要素)側で1つずつ指定

特定の要素だけ中央に寄せたい時はこちら。

- 横方向の中央 → `justify-self: center;`
- 縦方向の中央 → `align-self: center;`
- 両方まとめて → `place-self: center;`

```css
.item {
  place-self: center; /* この要素だけ中央に */
}
```

### flexとの違いに注意

flexだと「縦軸=align」「横軸=justify」が `flex-direction` によって入れ替わるが、Gridでは固定。

- `justify-` → 横(行方向)
- `align-` → 縦(列方向)
