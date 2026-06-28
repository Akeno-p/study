// エラーハンドリング(例外処理)について

try {
  // tryの中にエラーが起きるかもしれない処理を書く
  console.log(undefinedFunction);
  // catchにはエラー情報が渡されるので受け取る変数名を書く(慣習はe)
} catch (e) {
  // catchの中にエラーが起きた時に走らせたい処理を書く
  console.log(e.message); // エラーメッセージ本文
  console.log(e.name); // エラーの種類名
  console.log(e.stack); // エラー発生場所
} finally {
  // finallyの中にエラーの有無に関わらずからなず実行したい処理を書く
  console.log("毎回走らせたい処理");
}

//　自分でエラーを定義したい時
try {
  let num1 = -1;
  if (num1 < 0) {
    throw new Error("0以上の整数を入力してください");
  }
} catch (e) {
  console.log(e.message);
}
