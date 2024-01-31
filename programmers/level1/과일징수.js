function solution(k, m, score) {
    var answer = 0;
    return answer;
}
var answer = 0;

let k = 4;
let m = 3;
let score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	


let box = [];

//(Math.floor(score.length / m) * m)  //들어갈수있는 과일 갯수

score.sort(function(a, b)  {
    return b-a;
  });

for(s of score){
    if(s <= k){
        if(box.length >= (Math.floor(score.length / m) * m)) break;
        box.push(s);
    } 

    if(box.length === m){
        answer += box.at(-1) * m;
        box = [];
    }
}


console.log(box);
console.log(answer);
