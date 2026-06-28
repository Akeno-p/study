// Bool値(真偽値)について

// true or false　のもの。
// pythonと違って全て小文字なので注意

let num1 = 10;
let num2 = 6;

let isNum = num1 === num2;
console.log(isNum);

// falseとして扱われるものをfalsyという。
// falsyには以下のようなものがある

let ver1 = false;
let ver2 = 0;
let ver3 = "";
let ver4 = null;
let ver5 = undefined;
let ver6 = NaN;

if (ver1) {
  alert("これはtrueです");
} else {
  alert("これはfalseです");
}
