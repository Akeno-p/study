# BEM（命名規則）

CSSのクラス名に「ルール」を持たせて、誰が書いても迷わないようにするための命名規則。

`Block` / `Element` / `Modifier` の3つに分けて考える、という頭文字。

```text
block__element--modifier
  ↑       ↑         ↑
 ブロック  要素     状態違い
```

セマンティック（意味ベース）にクラス名を付ける時の、定番の書き方。

## ✒️Block（かたまり）

それ単体で意味が成り立つ「部品のかたまり」のこと。

```html
<div class="card"></div>
<form class="search-form"></form>
<nav class="global-nav"></nav>
```

`card`（カード）`search-form`（検索フォーム）のように、その部品を表す名前を付ける。

ページのどこに置いても、それ単体で意味が分かる単位。

## ✒️Element（中の要素）

Blockの中に入っている、それ単体では意味を持たないパーツのこと。

Blockの名前の後ろに `__`（アンダーバー2つ）でつなげる。

```html
<div class="card">
  <img class="card__image" />
  <h2 class="card__title">タイトル</h2>
  <p class="card__text">本文</p>
</div>
```

`card__title` は「カードの中のタイトル」という意味。

`card` の外に出すと意味を持たないものは、Elementとして扱う。

## ✒️Modifier（状態・種類違い）

同じBlock（またはElement）の「色違い」「サイズ違い」「状態違い」を表すパーツ。

`--`（ハイフン2つ）でつなげる。

```html
<button class="button button--primary">送信</button>
<button class="button button--disabled">送信</button>
```

```html
<div class="card card--large">
  <h2 class="card__title card__title--bold">タイトル</h2>
</div>
```

Modifierは、ベースのクラスと「一緒に」付けて使う。`button--primary` だけを書くのではなく、`button button--primary` と並べる。

## ✒️書き方のまとめ

```text
block            → かたまりの名前
block__element   → かたまりの中のパーツ
block--modifier  → かたまりの状態違い
block__element--modifier → パーツの状態違い
```

```css
.card {
}
.card__title {
}
.card--large {
}
.card__title--bold {
}
```

ネストや子セレクタ（`.card .title` のような書き方）は使わず、すべてフラットなクラス名で書くのがBEMの基本。

## ✒️思想

BEMがやりたいのは、「クラス名を見ただけで、それがどこの何かが分かる」状態にすること。

```html
<!-- ❌ どこの title か分からない -->
<h2 class="title"></h2>

<!-- ⭕ card の中の title だと一目で分かる -->
<h2 class="card__title"></h2>
```

- どのBlockに属するかが名前で分かる
- 他のページに同じ部品をコピーしても、スタイルが壊れない
- CSSの詳細度（specificity）が一定になり、上書き合戦が起きにくい

「意味ベースでクラスを付けたい」「部品を使い回したい」という時、まずBEMを採用しておけば大きく外すことはない。

## ✒️ユーティリティファースト（Tailwindなど）との違い

最近は、BEMのような「意味ベースの命名」とは別の流れも広がっている。代表が **Tailwind CSS** のような「ユーティリティファースト」のやり方。

```html
<!-- BEM：意味で名付けて、CSSは別ファイル -->
<div class="card">
  <h2 class="card__title">タイトル</h2>
</div>

<!-- Tailwind：見た目の指定をクラスで直接書く -->
<div class="rounded-lg shadow-md p-4">
  <h2 class="text-xl font-bold">タイトル</h2>
</div>
```

|             | BEM                                  | ユーティリティファースト             |
| ----------- | ------------------------------------ | ------------------------------------ |
| クラス名    | 意味で付ける                         | 見た目を直接書く                     |
| CSSファイル | 自分で書く                           | ほぼ書かない                         |
| 強み        | 意味が伝わる・部品単位で管理しやすい | 書くのが速い・CSSが膨らまない        |
| 弱み        | クラス設計に時間がかかる             | HTMLが長くなる・意味が読み取りにくい |

どちらが正解というよりは、プロジェクトの方針で選ぶもの。

- 自分でCSSを設計したい、意味のあるマークアップにしたい → **BEM**
- とにかく速く作りたい、CSSを書く量を減らしたい → **Tailwindなどのユーティリティファースト**

学習の段階では、まずBEMで「意味ベースの設計」に慣れておくと、後でTailwindに移っても「このクラスのかたまりは何のためのものか」を整理しやすい。
