// for文について

// for(初期化処理; ループ継続の条件式; ループごとの最後に実行される式)
for (let num = 2; num < 10; num += 2) {
  console.log("値は" + num + "です");
}

// 初期化や条件式、実行される式などは省略することができる
let num2 = 3;
for (; num2 < 20; ) {
  console.log("値は" + num2 + "です");
  num2 += 3;
}

// 配列を使用したfor文
let arr = ["りんご", "みかん", "ぶどう"];
for (let i = 0; i < arr.length; i += 1) {
  console.log(arr[i]);
}

// for of とすることでキーを取り出すことができる
for (const val of arr) {
  console.log("値は" + val + "です");
}

// オブジェクトを使用したfor文
// for in とすることでキーを取り出すことができる
let obj = { name: "高橋", age: 24, job: "エンジニア" };
for (const key in obj) {
  console.log("キーは" + key + "です");
  console.log("値は" + obj[key] + "です");
}
