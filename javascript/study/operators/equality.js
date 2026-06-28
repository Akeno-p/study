// 等価演算子について

// == 値が正しいことを確認

let bool1 = 1 == "1"; // 型が str
let bool2 = 1 == 1; //型が  int

// 両方trueになる
console.log(bool1);
console.log(bool2);

// === 型と値が正しいことを確認

let bool3 = 1 === "1"; // 型が str
let bool4 = 1 === 1; //型が  int

// bool3はfalseになる
console.log(bool3);
console.log(bool4);

// != 値が正しくないことを確認
let bool5 = 1 != "1"; // 型が str
let bool6 = 1 != 1; //型が  int

// 両方falseになる
console.log(bool5);
console.log(bool6);

// !== 型と値が正しくないことを確認
let bool7 = 1 !== "1"; // 型が str
let bool8 = 1 !== 1; //型が  int

// bool7だけtrueになる
console.log(bool7);
console.log(bool8);
