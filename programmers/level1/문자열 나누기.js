let s = 'aaabbaccccabba';
let result = [];
let idx = 0;

while (idx < s.length) {
    let v = Array.from(s.slice([idx]));
    let i = 0;

    let 주count = 1;
    let 부count = 0;
    
    while(true){
        console.log(v[i+1])
        if(v[0] === v[i+1]) 주count++;
        if(v[0] !== v[i+1]) 부count++;
    
        if(주count === 부count){
            result.push(v.slice(0,주count+부count));
            idx += (주count+부count);
            break;
        }
        i++
    }

    
}


/**
 * 좋은 풀이라고 생각되는 부분
 */
let answer = 0;
let current;
let count = 0;

for(let i = 0; i < s.length; i++) {
    if(count === 0) {
        answer++;
        current = s[i]
        count = 1
    } else {
        console.log(current);
        console.log(s[i]);
        if(current !== s[i]) count--;
        else count++;
    }
}

