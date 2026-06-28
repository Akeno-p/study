# フォームについて

## ⭐️label

入力欄の説明を書くタグ。
`p`タグではなく、基本的には`label`を使う。

```html
<label for="name">名前</label> <input id="name" type="text" />
```

`label`の`for`には、対象のフォーム部品の`id`を書く。
`class`や`name`ではなく、`id`と紐づく。

```html
<label for="email">メールアドレス</label> <input id="email" type="email" />
```

ラベルをクリックすると、紐づいた入力欄にフォーカスできる。
スクリーンリーダーにも「この入力欄が何の入力欄なのか」が伝わりやすい。

### ✒️labelの書き方

よく使うのは、`for`と`id`で紐づける書き方。

```html
<label for="password">パスワード</label> <input id="password" type="password" />
```

`label`の中に`input`を入れる書き方もある。
特に`checkbox`や`radio`で見かける。

```html
<label>
  <input type="checkbox" />
  利用規約に同意する
</label>
```

基本は`label for` + `id`。
`checkbox`や`radio`では、`label`の中に入れる書き方もよく使われる。

## ⭐️input

1行入力、チェックボックス、ラジオボタンなどを作るタグ。
`type`属性で入力の種類を変える。

```html
<input type="text" />
<input type="email" />
<input type="password" />
```

`type`を書かない場合は、基本的に`type="text"`として扱われる。
ただし、実務では分かりやすいので`type="text"`と明記することが多い。

```html
<input /> <input type="text" />
```

### ✒️よく見るinput type

```html
<input type="text" />
<input type="email" />
<input type="password" />
<input type="number" />
<input type="tel" />
<input type="checkbox" />
<input type="radio" />
<input type="file" />
<input type="hidden" />
<input type="submit" />
```

| type       | 用途                   |
| ---------- | ---------------------- |
| `text`     | 普通の1行テキスト      |
| `email`    | メールアドレス         |
| `password` | パスワード             |
| `number`   | 数値                   |
| `tel`      | 電話番号               |
| `checkbox` | 複数選択・同意チェック |
| `radio`    | 1つだけ選択            |
| `file`     | ファイルアップロード   |
| `hidden`   | 画面に出さない値       |
| `submit`   | フォーム送信ボタン     |

電話番号は`number`ではなく、`tel`を使うことが多い。
先頭の`0`やハイフンを扱いやすいため。

```html
<input type="tel" />
```

`submit`はフォーム送信用のボタン。
最近は`button`タグで書くことも多い。

```html
<!--buttonタグでの書き方↓-->
<button type="submit">送信</button>
```

### ✒️inputでよく使う属性

`input`で実務的に理解しておきたい属性。

```html
<input type="text" placeholder="山田太郎" required />
<input type="text" value="初期値" />
<input type="text" required />
<input type="checkbox" checked />
<input type="text" disabled />
<input type="text" readonly />
<input type="text" maxlength="20" />
<input type="number" min="1" max="99" />
<input type="file" accept="image/*" />
```

| 属性          | type                 | 意味                                 |
| ------------- | -------------------- | ------------------------------------ |
| `placeholder` | 入力欄がある系       | 入力前に薄く表示される入力例・ヒント |
| `value`       | ほぼ全て             | 初期値、または送信される値           |
| `required`    | ほぼ全て             | 必須入力にする                       |
| `checked`     | `checkbox` / `radio` | 最初から選択済みにする               |
| `disabled`    | ほぼ全て             | 操作できない状態にする               |
| `readonly`    | 入力欄がある系       | 表示はするが編集できない状態にする   |
| `maxlength`   | 文字や数字入力系     | 入力できる最大文字数                 |
| `min` / `max` | `number`             | 数値の最小値・最大値                 |
| `accept`      | `file`               | 受け取るファイルの種類を指定する     |

**※ typeはあくまで例。正確な仕様は都度確認**

## ⭐️textarea

複数行の文章を入力するためのタグ。
お問い合わせ内容、コメント、備考欄、自己紹介文などで使う。

```html
<label for="message">お問い合わせ内容</label> <textarea id="message"></textarea>
```

`input type="text"`は1行入力。
`textarea`は複数行入力。

```html
<input type="text" /> <textarea></textarea>
```

`textarea`は開始タグと終了タグがある。
初期値を書く場合は、`value`属性ではなくタグの中に書く。

```html
<textarea>初期値</textarea>
```

### ⚠️textareaの注意点

`textarea`はタグの中の改行やスペースも入力値として扱う。
見やすくしようとして改行したり、フォーマッターで整形されたりすると、余計なスペースが入ることがある。

```html
<textarea>
  初期値
</textarea>
```

この場合、`初期値`の前後の改行やスペースも値に含まれる。
初期値を書くなら、開始タグと終了タグの間にそのまま書く方が安全。

```html
<textarea>初期値</textarea>
```

### ✒️textareaでよく使う属性

`textarea`で実務的に理解しておきたい属性。

```html
<textarea placeholder="お問い合わせ内容を入力してください"></textarea>
<textarea required></textarea>
<textarea maxlength="1000"></textarea>
<textarea rows="5"></textarea>
<textarea readonly>編集できない内容</textarea>
<textarea disabled>操作できない内容</textarea>
```

| 属性          | 意味                                 |
| ------------- | ------------------------------------ |
| `placeholder` | 入力前に薄く表示される入力例・ヒント |
| `required`    | 必須入力にする                       |
| `maxlength`   | 入力できる最大文字数                 |
| `rows`        | 表示する行数                         |
| `readonly`    | 表示はするが編集できない状態にする   |
| `disabled`    | 操作できない状態にする               |

`cols`もあるが、横幅はCSSで調整することが多い。

```css
/* cssで指定する例 */
textarea {
  width: 100%;
}
```

## ⭐️select

選択肢の中から1つを選ばせるためのタグ。
プルダウンを作るときに使う。

```html
<label for="prefecture">都道府県</label>
<select id="prefecture">
  <option value="tokyo">東京</option>
  <option value="osaka">大阪</option>
</select>
```

`select`が選択欄。
選択肢は`option`で書く。
`option`は基本的に`select`の中で使う。

```html
<select>
  <option>選択肢1</option>
  <option>選択肢2</option>
</select>
```

### ✒️optionのvalue

`option`の`value`は、送信される値。

```html
<option value="yes">はい</option>
```

画面には`はい`と表示されるが、送信される値は`yes`。

`value`を書かなかった場合は、`option`の中のテキストがそのまま値になる。

```html
<option>はい</option>
```

この場合、送信される値は`はい`。
実務では、送信値を分かりやすくするために`value`を書くことが多い。

### ✒️未選択状態

`select`は何もしないと、最初の`option`が選択された状態になる。
未選択状態を作りたい場合は、先頭に空の`option`を置く。

```html
<select>
  <option value="">未選択</option>
  <option value="yes">はい</option>
  <option value="no">いいえ</option>
</select>
```

案内用にして選ばせたくない場合は、`disabled`を使う。

```html
<select>
  <option value="" selected disabled>選択してください</option>
  <option value="yes">はい</option>
  <option value="no">いいえ</option>
</select>
```

ただし、`disabled`にすると、その項目には戻れない。
未選択に戻せるようにしたい場合は、`disabled`を付けない。

### ✒️selectでよく使う属性

`select`と`option`で実務的に理解しておきたい属性。

```html
<select required>
  <option value="">選択してください</option>
  <option value="yes">はい</option>
  <option value="no">いいえ</option>
</select>

<select disabled>
  <option value="yes">はい</option>
</select>

<select multiple>
  <option value="html">HTML</option>
  <option value="css">CSS</option>
</select>
```

| 属性       | 使う場所            | 意味                     |
| ---------- | ------------------- | ------------------------ |
| `value`    | `option`            | 送信される値             |
| `selected` | `option`            | 最初から選択済みにする   |
| `disabled` | `select` / `option` | 選択できない状態にする   |
| `required` | `select`            | 必須選択にする           |
| `multiple` | `select`            | 複数選択できるようにする |

`required`は`option`ではなく、`select`に付ける。

```html
<select required>
  <option value="">選択してください</option>
  <option value="yes">はい</option>
  <option value="no">いいえ</option>
</select>
```

`multiple`は使えるが、UIが少し分かりにくい。
実務では`checkbox`で代用することも多い。

## ⭐️button

クリックできるボタンを作るタグ。
フォームでは送信ボタン、キャンセルボタン、JSで処理するボタンなどで使う。

```html
<button type="submit">送信</button> <button type="button">キャンセル</button>
```

### ✒️buttonのtype

| type     | 意味                         |
| -------- | ---------------------------- |
| `submit` | フォームを送信する           |
| `button` | ただのボタン。JSなどで使う   |
| `reset`  | フォームの入力内容をリセット |

`form`の中の`button`は、`type`を書かないと基本的に`submit`扱いになるが、
事故防止とわかりやすさ目的で省略せず`submit`と書くことが多い。

送信しないボタンなら、`type="button"`を書く方が安全。

```html
<button type="button">クリック</button> <button type="submit">送信</button>
```

### ✒️buttonでよく使う属性

`button`で実務的に理解しておきたい属性。

```html
<button type="submit">送信</button>
<button type="button">普通のボタン</button>
<button type="submit" disabled>送信できない</button>
<button type="submit" name="action" value="save">保存</button>
```

### ✒️ nameとvalueについて

nameとvalueを設定することでname=valueという形式でデータを送れる。

`button`で`name`と`value`を使うと、どのボタンが押されたかを判別できる。

```html
<button type="submit" name="action" value="save">保存</button>
<button type="submit" name="action" value="delete">削除</button>
```

保存を押すと`action=save`。
削除を押すと`action=delete`。

#### nameとvalueどちらかだけしか書かなかった場合の挙動

| 書き方           | 送信される内容                       |
| ---------------- | ------------------------------------ |
| `value`だけ      | 送信されない                         |
| `name`だけ       | `name=`として送信 (例：action=)      |
| `name` + `value` | `name=value`で送信 (例：action=save) |

### ✒️input type="button"との違い

`button`タグは、中に文字やHTMLを入れられる。

```html
<button>
  <span>保存</span>
</button>
```

`input type="button"`は中にHTMLを入れられない。
表示文字は`value`で指定する。

```html
<input type="button" value="保存" />
```

実務では、アクセシビリティや可読性の観点から
基本的に`button`タグを使うことが多い。
