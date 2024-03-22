function solution(absolutes, signs) {
    var answer = 123456789;
    return answer;
}


let answer = 0;

let absolutes = [4,7,12];
let signs = [true,false,true];


for(let i = 0; i < absolutes.length; i++){

    signs[i] == true ? answer += absolutes[i]  : answer += -(absolutes[i])

}

console.log(answer);