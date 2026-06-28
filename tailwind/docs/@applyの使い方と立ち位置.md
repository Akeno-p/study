# @apply の使い方と立ち位置

## @apply とは

Tailwind のユーティリティクラスを CSS ファイル側でまとめて、セマンティックなクラス名を作れる機能。

```css
/* CSS ファイル */
.btn {
  @apply rounded bg-blue-500 px-4 py-2 text-white;
}
```

```html
<!-- HTML 側はクラス名だけで済む -->
<button class="btn">送信</button>
```

Tailwind がビルド時に `@apply` を展開して、通常の CSS プロパティに変換する。

```css
/* 展開後 */
.btn {
  background-color: #3b82f6;
  color: white;
  padding-left: 1rem;
  padding-right: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  border-radius: 0.25rem;
}
```

## 公式の立場：あまり推奨していない

Tailwind 公式は `@apply` の多用を推奨していない。理由は、**Tailwind のメリットを自分で打ち消す行為**だから。

| Tailwind のメリット           | @apply を使うと                        |
| ----------------------------- | -------------------------------------- |
| HTML を見ればスタイルが分かる | CSS ファイルを見に行く必要が復活する   |
| 命名コストゼロ                | `.btn` 等の名前を考える作業が復活する  |
| 削除すれば CSS も消える       | CSS に残ったクラスが死コードになりうる |
| 変更の影響範囲がその場で完結  | クラスを使っている全箇所に影響が広がる |

コンポーネント環境（React / Vue 等）であれば、`@apply` で `.btn` クラスを作るよりも `<Button>` コンポーネントを作る方が Tailwind の思想に合っている。

```jsx
// 公式が推奨するアプローチ
function Button({ children }) {
  return (
    <button className="rounded bg-blue-500 px-4 py-2 text-white">
      {children}
    </button>
  );
}
```

## それでも現実的に使われるケース

### コンポーネント環境がないプロジェクト

React / Vue を使っていない環境では、HTML のコンポーネント化ができない。同じユーティリティクラスの羅列を何箇所にも書くのは現実的ではないので、`@apply` でまとめるのは合理的な妥協。

```css
/* コンポーネント化できないなら、CSS 側でまとめるしかない */
.btn {
  @apply rounded bg-blue-500 px-4 py-2 text-white;
}

.btn--danger {
  @apply bg-red-500;
}
```

```html
<button class="btn">送信</button> <button class="btn btn--danger">削除</button>
```

実質的に **BEM + Tailwind のデザイントークン** という運用になる。

### 将来の移行を見据えたアプローチ

「今はコンポーネント環境がないけど、将来 React 等に移行するかもしれない」という場合：

1. Tailwind を導入し、`@apply` + BEM で運用する
2. 移行時に `@apply` の中身をそのままコンポーネントに持っていく

この流れなら、Bootstrap → Tailwind → React + Tailwind という段階的な移行がしやすい。

## @apply を使うときに意識すべきこと

- **Tailwind の主要メリット（コロケーション・命名コストゼロ・削除の安全性）は使えていない**ことを理解しておく
- 実質的には **Sass + デザイントークンに近いこと**をしている
- 「わかった上であえてこう選んだ」という判断であれば問題ない

## まとめ

| 観点           | 内容                                                            |
| -------------- | --------------------------------------------------------------- |
| @apply の役割  | ユーティリティクラスを CSS 側でセマンティックなクラスにまとめる |
| 公式の推奨     | コンポーネント環境なら使わず、コンポーネントで再利用すべき      |
| 現実の使われ方 | コンポーネント環境がないプロジェクトでは実用的な選択肢          |
| 本質           | Tailwind のデザイントークンを活かしつつ、BEM 的な運用をする手段 |
| 注意点         | Tailwind の主要メリットは失われることを理解した上で使う         |
