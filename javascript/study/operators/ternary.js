// 三項演算子について

bool1 = true;
bool2 = false;
bool3 = 0;
bool4 = "テスト";

bool4
  ? alert("これはtrueの時に実行される")
  : alert("これはfalseの時に実行される");

userName = "田中";

userName
  ? alert("ユーザー名: " + userName + " が登録されました。")
  : alert("ユーザー名を入力してください");

if (userName) {
  alert("ユーザー名: " + userName + " が登録されました。");
} else {
  alert("ユーザー名を入力してください");
}

70 > 20 ? alert("test") : alert("あああ");
