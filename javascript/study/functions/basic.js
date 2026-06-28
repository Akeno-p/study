// 関数の基本について

let test = 100;
let a = Number(prompt("値Aを入力してください"));
let b = Number(prompt("値Aに対して計算を行う値Bを入力してください"));
// 基本的な書き方
function example() {
  console.log("入力した値は" + a + "です");
}

example();

// returnを書くとその値が帰る。
// 引数にデフォルト値を登録することもできる
function orya(a, b = 5) {
  let sum = a + b;
  let difference = a - b;
  let product = a * b;
  let quotient = a / b;
  console.log("足し算結果" + sum);
  console.log("引き算結果" + difference);
  console.log("掛け算結果" + product);
  console.log("割り算結果" + quotient);
  return sum;
}

// 戻り値を使用することができる
let ret = orya(a);
console.log("これ戻り値で出してる" + ret);

function test(a = 3) {
  let b = a + 5;
  return b;
}