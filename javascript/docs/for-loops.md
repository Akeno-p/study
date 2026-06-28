# for文について

JavaScriptのfor文は3種類ある。

## 3種類のfor文

```js
// クラシックな for
for (let i = 0; i < 5; i += 1) {
  console.log(i);
}

// for...in → キーを取り出す
let obj = { name: "田中", age: 24 };
for (const key in obj) {
  console.log(key); // → "name", "age"
  console.log(obj[key]); // → "田中", 24
}

// for...of → 値を取り出す
let arr = ["りんご", "みかん"];
for (const val of arr) {
  console.log(val); // → "りんご", "みかん"
}
```

## for...in と　for...of どちらを使うか？

- オブジェクト → `for...in` で **キー** を取り出す
- 配列 → `for...of` で **値** を取り出す

## 注意点

- `for...of` はオブジェクトに使えない。エラーになる(`TypeError`)
- オブジェクトの値だけ欲しい時は `Object.values(obj)` をつかう
- 配列に `for...in` は使えるが、推奨されない(順序が保証されないなど)
