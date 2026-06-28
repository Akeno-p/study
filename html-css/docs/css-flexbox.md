# 配置などについて

## display: flex;

- まずはこれを使って並び替えができる状態にする。そこから色々設定してくイメージ

## flex-direction:

コンテンツの並び方

```css
flex-direction: row; /* 横並び 初期値 */
flex-direction: column; /* 縦並び */
```

## justify-content:

並びをどうするか？の話
※ コンテンツの並びがrowなのかcolumnなのかで、横に対してなのか、縦に対してなのか変わる

```css
justify-content: flex-start; /* 左(上)寄せ 初期値 */
justify-content: center; /* 中央寄せ */
justify-content: flex-end; /* 右(下)寄せ */
justify-content: space-between; /* 両端に寄せて、間を均等に空ける */
justify-content: space-around; /* 各要素の左右に余白をつける */
justify-content: space-evenly; /* すべての余白を均等にする */
```

## align-items:

交差する方向にどう揃えるか？の話
※ コンテンツの並びがrowなのかcolumnなのかで、横に対してなのか、縦に対してなのか変わる
簡単にいうと、justify-contentが横なら縦、縦なら横

```css
align-items: stretch; /* 交差軸方向にいっぱいに広げる 初期値 */
align-items: flex-start; /* 上(左)揃え */
align-items: center; /* 中央揃え */
align-items: flex-end; /* 下(右)揃え */
```

## gap:

コンテンツ同士の隙間をどれくらい空けるか？の話
※ paddingでもmarginでもなく、並んでいる子要素同士の間にできる隙間

```css
gap: 10px; /* 子要素同士の隙間を10px空ける */
gap: 20px; /* 子要素同士の隙間を20px空ける */
```
