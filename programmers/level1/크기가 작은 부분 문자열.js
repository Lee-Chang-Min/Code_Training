function solution(t, p) {
    var answer = 0;
    return answer;
}


let t = "3141592";
let p = "271";

let answer = 0;

// console.log(p.length);

// console.log(t.slice(0,p.length))
// console.log(t.slice(3,3+p.length))
// console.log(Number(t.slice(4,4+p.length)))
// console.log(t.slice(5,5+p.length))

for(let i = 0; i<t.length; i++){
    if(t.slice(i,i+p.length).length < p.length) break;
    console.log( Number((t.slice(i,i+p.length))) );
    
    if(p >= Number((t.slice(i,i+p.length)))){
        answer++
    }
}

/*
두번째 방법
*/

function solution(t, p) {
    let count = 0;
    for(let i=0; i<=t.length-p.length; i++) {
        let value = t.slice(i, i+p.length);
        if(+p >= +value) count++;
    }
    return count;
}

console.log(answer);








