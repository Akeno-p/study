// continue文について
// 途中で処理をやめて次のループに行く

let num = 0;
while (num < 10) {
  num += 1;
  if (num % 2 === 0) {
    continue;
  }
  console.log(num + "は奇数です");
}






