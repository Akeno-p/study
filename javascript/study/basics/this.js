// thisについて
// thisは「この関数を呼び出しているオブジェクトを参照する」キーワード

// 基本的な使い方
const dog = {
  name: "ポチ",
  bark: function () {
    console.log(this.name + "だワン"); // this = dog
  },
};

const cat = {
  name: "タマ",
  meow: function () {
    console.log(this.name + "だニャン"); // this = cat
  },
};

dog.bark(); // "ポチだワン"
cat.meow(); // "タマだニャン"

// 通常の関数とアロー関数でthisの挙動が異なる
const obj = {
  name: "太郎",
  // 通常の関数：呼び出したオブジェクト（obj）がthis
  greet: function () {
    console.log(this.name); // "太郎"
  },
  // アロー関数：外側のthisをそのまま使う（定義した場所のthis）
  greetArrow: () => {
    console.log(this.name); // undefined（外側 = グローバルのthis）
  },
};

obj.greet(); // "太郎"
obj.greetArrow(); // undefined
