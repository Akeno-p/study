// if文について

let num1 = 1;
let num2 = 2;
let num3 = 1;

// if文はこのように書く
if (num1 < num2) {
  alert("num2の方が大きいです。");
}

// 条件が沢山あるとき & falsyの時の処理を書く場合
if (num1 === num2) {
  alert("num1とnum2は同じ値です。");
} else if (num1 === num3) {
  alert("num1とnum3は同じ値です。");
} else {
  alert;
  ("num1はどの値とも一致しません。");
}

// 論理演算子を使って条件を書くこともできる
if (num1 === num2 && num1 === num3) {
  alert("num2とnum3はnum1と同じ値です");
} else if (num1 === num2 || num1 === num3) {
  alert("num2とnum3のどちらかは、num1と同じ値です");
} else {
  ("num1はどの値とも一致しません。");
}
