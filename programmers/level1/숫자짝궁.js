function solution(X, Y) {
    var answer = '';
    return answer;
}

let X = "100"
let Y = "123450"

// yArray =  Array.from(y)

// let answer = [];

// for(xIdx in x){
//     //console.log(xIdx);
    
//     yArray.find((yValue, i) => {
//         //console.log(Array.from(x)[xIdx]);
//         console.log(yValue);
        
//         if(Array.from(x)[xIdx] === yValue)
//         {
//             answer.push(yValue);
//             yArray.splice(i,1);
//         }
//     })
// }

// answer = answer.sort((a,b) => (b-a))

const hashX = new Map();
const hashY = new Map();

for (const digit of X) {
  hashX.set(digit, (hashX.get(digit) || 0) + 1);
}
for (const digit of Y) {
  hashY.set(digit, (hashY.get(digit) || 0) + 1);
}

let answer = '';
for (let i = 9; i >= 0; i--) {
  const char = String(i);
  const count = Math.min(hashX.get(char), hashY.get(char));
  answer += char.repeat(count);
}
return answer ? (Number(answer) ? answer : '0') : '-1';