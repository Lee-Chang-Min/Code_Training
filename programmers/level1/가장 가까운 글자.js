function solution(s) {
    var answer = [];
    return answer;
}

var answer = [];
let s = 'banana'

console.log(Array.from(s))
Array.from(s).forEach((e, idx)=> {
    let n = 0;
    let f = answer.length
    while(s[idx-1] !== undefined){
        n++
        console.log( s[idx-1]);
        if(e == s[idx-1]) {
            answer.push(n); 
            break;
        }
        idx--;
    }
    let l = answer.length
    if(f == l) answer.push(-1)
});

console.log(answer);
