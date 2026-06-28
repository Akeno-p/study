// コールバック関数について

function piyo(num1, num2) {
  let sum1 = num1 + num2;
  return sum1;
}

// コールバック関数
function kotae(callback, num1, num2) {
  let result = callback(num1, num2);
  console.log("答えは" + result + "です。");
}

kotae(piyo, 2, 3);

const dorya = function () {
  console.log("こんにちわ");
};

// 無名関数
kotae(
  function (x, y) {
    let result = x - y;
    return result;
  },
  20,
  30,
);

