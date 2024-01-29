function solution(k, score) {
    var answer = [];
    return answer;
}

let k = 3
let score = [10, 100, 20, 150, 1, 100, 200];

let now = []; 
let answer = [];

for(s of score){
    now.push(s);
    now.sort(function(a, b)  {
        return b - a;
      });
    
    if(now.length>3){
        now.pop();
    }

    answer.push(now.at(-1));

}

console.log(answer);
