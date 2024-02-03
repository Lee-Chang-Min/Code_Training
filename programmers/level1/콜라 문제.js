function solution(a, b, n) {
    var answer = 0;
    return answer;
}

answer = 0;

let a = 5;
let b = 3;
let n = 21;

while(n >= a){
    
    //교환해서 받은 병수
    console.log(((Math.floor(n/a) * a) / a) * b);
    answer += ((Math.floor(n/a) * a) / a) * b;
    
    //교환하고 집에 남은 병수
    n = n - (Math.floor(n/a) * a) + (((Math.floor(n/a) * a) / a) * b);
}

