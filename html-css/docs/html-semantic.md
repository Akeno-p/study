# Semantic HTML

HTMLでは、ただの箱として `div` を使うこともできる。

```html
<div class="header"></div>
<div class="main"></div>
<div class="footer"></div>
```

ただし、役割が決まっている場所では専用のタグを使う方が分かりやすい。

```html
<header></header>
<main></main>
<footer></footer>
```

## divとの違い

`div` は意味を持たない箱。

`header` / `main` / `footer` は意味を持つ箱。

- `header`: ページやセクションの上部
- `main`: ページの主な内容
- `footer`: ページやセクションの下部

見た目はほぼ同じで、CSSを書かない限り特別なデザインはつかない。

## 基本

`header` / `main` / `footer` にあたる場所では、専用のタグを使う。

細かい配置やグループ分けには `div` を使う。
