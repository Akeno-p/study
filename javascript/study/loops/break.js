// break文について
// breakを使用することでブロック内の処理を抜けることができる

let num = 1;
while (true) {
  console.log(num);
  num += 1;
  if (num === 10) {
    break;
  }
}
