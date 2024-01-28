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

console.log(result.length)
//answer += result.length;


