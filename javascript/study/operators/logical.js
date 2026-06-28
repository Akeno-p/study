// 論理演算子について

const isA = true;
const isB = false;
const isC = true;
const isD = false;

// && 論理積(and条件)について

// trueとfalse
let bool1 = isA && isB;
console.log(bool1); // false

// trueとtrue
let bool2 = isA && isC;
console.log(bool2); // true

// falseとfalse
let bool3 = isB && isD;
console.log(bool3); // false

// || 論理和(or条件)について
// trueとfalse
let bool4 = isA || isB;
console.log(bool4); // true

// trueとtrue
let bool5 = isA || isC;
console.log(bool5); // true

// falseとfalse
let bool6 = isB || isD;
console.log(bool6); // false
