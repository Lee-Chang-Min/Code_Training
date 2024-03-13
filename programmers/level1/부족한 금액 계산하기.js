function solution(price, money, count) {
    var answer = -1;

    return answer;
}

// 1 ≤ price ≤ 2,500,
//1 ≤ count ≤ 2,500
//1 ≤ money ≤ 1,000,000,000, 

let price = 3
let money = 20
let count = 4
var answer = -1;

for (let c = 1; c <= count; c++){
    money -= price * c;
}

if(money < 0){
    answer = -1 * money
}else{
    answer = 0
}

console.log(answer);
