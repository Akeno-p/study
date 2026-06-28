// 関係演算子について

// A < B AがBより小さいか？
//  > は逆
let bool1 = 1 < 2;
let bool2 = 1 < 1;
console.log(bool1); // true
console.log(bool2); // false

// A <= B AがBより小さいか？
//  >= は逆
let bool3 = 1 <= 2;
let bool4 = 1 <= 1;
console.log(bool3); // true
console.log(bool4); // true

// A in B AがBのオブジェクトのキーに含まれるか？
let bool5 = "job" in { job: "教師" };
let bool6 = "教師" in { job: "教師" };
console.log("===ここからinについて===");
console.log(bool5); // true
console.log(bool6); // false

// !について
// !をつけると真偽値がひっくり返る
let bool7 = !true;
let bool8 = !false;
console.log("===ここから!について===");
console.log(bool7); //false
console.log(bool8); //true
