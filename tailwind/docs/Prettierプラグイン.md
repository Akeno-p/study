# Prettier プラグイン（prettier-plugin-tailwindcss）

## 何をしてくれるか

Tailwind のクラスを**推奨順に自動ソート**してくれる。保存するだけでクラスの並び順が統一される。

```html
<!-- ソート前（バラバラ） -->
<div class="flex rounded bg-sky-500 p-4 font-bold text-white">
  <!-- ソート後（自動で整列） -->
  <div class="flex rounded bg-sky-500 p-4 font-bold text-white"></div>
</div>
```

並び順はレイアウト → サイズ → 装飾 → テキスト → 状態 のような順番になる。

## インストール

```bash
npm install -D prettier prettier-plugin-tailwindcss
```

`-D` は開発用の依存関係としてインストールするオプション。本番には不要なツールなので `-D` を付ける。

## 設定ファイル

プロジェクトルートに `.prettierrc` を作成する。

```json
{
  "plugins": ["prettier-plugin-tailwindcss"]
}
```

## 設定ファイルの置き場所

| 場所                                  | 効果                       |
| ------------------------------------- | -------------------------- |
| プロジェクトルート（`.prettierrc`）   | そのプロジェクトだけに適用 |
| ホームディレクトリ（`~/.prettierrc`） | 全プロジェクトに適用       |

プロジェクトごとに設定が違うこともあるので、プロジェクトルートに置くのが一般的。
