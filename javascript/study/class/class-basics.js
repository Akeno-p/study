// クラスについて

class User {
  constructor(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;
  }
  userStatus() {
    console.log("ユーザー名:" + this.name);
    console.log("年齢:" + this.age);
    console.log("職業:" + this.job);
  }
}

const user1 = new User("tanaka", 24, "engineer");

user1.userStatus();

// 継承
class adminUser extends User {
  constructor(name, age, job, admin) {
    super(name, age, job);
    this.admin = admin;
  }
}
