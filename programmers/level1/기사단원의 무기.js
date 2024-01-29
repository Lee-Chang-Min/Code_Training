function solution(number, limit, power) {
    var answer = 0;
    return answer;
}

var answer = 0;

let number = 5;
let limit = 3;
let power = 2;

let 공격력 = [];

for(let 기사 = 1; 기사 <= number; 기사++){
    let count = 0;

    for(let j=1; j <= Math.sqrt(기사); j++){
        if(기사 % j === 0) {
            if (기사 / j === j) count += 1;
            else count += 2;
        }
    }
    공격력.push(count);
}

console.log(공격력);
for(공 of 공격력){
    공 > limit ? answer += power : answer += 공
}
//console.log(answer);