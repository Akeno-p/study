// よく目にするエラーについて

// ReferenceError
// 未定義の関数や変数を参照しようとした時に起こるエラー
console.log(undefinedFunction);

// SyntaxError
// 記法に間違いがある時に発生する
ig (false) { // ifのタイポ
  console.log("falseです");
}

// TypeError
// 期待した型じゃなかった時に発生する
let num = 123;
num(); // 関数じゃないものを関数のように呼ぶ
