// アロー関数 引数が0個
const allow = () => {
  const num = Number(prompt("数字を入力してください。"));
  const result = num / 2;
  return result;
};

// アロー関数 引数が1個
const allow1 = (x) => {
  const result1 = x / 2;
  return result1;
};

// 引数が一つの時は()を省略できる。
// prettier-ignore
const allow2 = x => {
  const result2 = x / 2;
  return result2;
};

// アロー関数　引数が2個以上
const allow3 = (x, y) => {
  const result3 = x + y;
  return result3;
};

const sum = allow3(10, 30);
console.log(sum);
