// label文について

// ループにラベル(名前)を付けて、break ラベル名 と書くと、
// そのラベルが付いたループを抜けることができるlet num = 1;
outer: while (true) {
  console.log(num);
  num += 1;
  while (num < 20) {
    num += 1;
    console.log(num);
    if (num === 10) {
      break outer;
    }
  }
}
