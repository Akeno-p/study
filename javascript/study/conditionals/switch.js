// switchについて

let num = 100;

switch (num) {
  case 20: // num === 20 が行われている
    alert("値は20です");
    break;
  case 100: // num === 100 が行われている
    alert("値は100です");
    break;
  default: // どれにも一致しない時の処理
    alert("値は20でも100でもありません。");
}

// switch文はbreakに出会うまで下のケースの処理を実行していくので注意する
// ↓ この場合、breakがないので全部実行される(フォロースルーという)
let num2 = 20;
switch (num2) {
  case 20:
    alert("値は20です");
  case 100:
    alert("値は100です");
  default:
    alert("値は20でも100でもありません。");
}
