// オブジェクトについて

let user = {
  name: "田中",
  age: 24,
  job: "エンジニア",
};

// ドットでオブジェクト名.キー名とすると値が取れる
console.log(user.age);

let key = "name";

// ドット記法では変数を使うことができない
console.log(user.key);

// ブラケット記法であれば、変数を使用することができる
console.log(user[key]);
console.log(user["name"]);

// delete オブジェクト.keyでプロパティを消すこともできる
delete user.age;
console.log(user);
/*
下記のようになる
{
    name: "田中",
    job: "エンジニア"
}
*/
