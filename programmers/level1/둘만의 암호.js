function solution(s, skip, index) {
    var answer = '';
    return answer;
}
var answer = '';
let s = "a"
let skip = "bcdefghijk"
let index = 20

var alphabet = { a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7, h: 8, i: 9, j: 10, k: 11, l: 12,
    m: 13, n: 14, o: 15, p: 16, q: 17, r: 18, s: 19, t: 20, u: 21, v: 22, w: 23, x: 24, y: 25, z: 26 };
    
function getKeyByValue(obj, value) {
    return Object.keys(obj).find(key => obj[key] === value);
 }
let pass = skip.split('');
var skiparray = [];
for(let c of pass){
    skiparray.push(alphabet[c]);
}
for (let i of s.split('')){
    var resarray = [];
    let cnt = 1;
    let value = Number(alphabet[`${i}`]);

    while(cnt !== index + 1){
        value++;
        if(value > 26) {value -= 26};

        pass.find((key) => {
            if(key === getKeyByValue(alphabet, value)) {
                value++
                if(value > 26) {value -= 26};
            };
        });

        resarray.push(getKeyByValue(alphabet, value).at(-1));
        cnt++
    }
    // let key = Object.keys(alphabet).find((key) => {
    //     if(value > 26) value - 26;
    //     return alphabet[key] === value;
    // });
    answer += resarray.at(-1);
    console.log(answer);
}

/*
* Set을 이용하여 몫을 구하는 방법으로 풀이
*/
function solution(strings, skip, index) {
    let answer = '';
    const alphabet = new Set('abcdefghijklmnopqrstuvwxyz');
    [...skip].forEach(val => alphabet.delete(val));
  
    const arr = [...alphabet];
  
    for (const s of strings) {
      const idx = arr.indexOf(s) + index;
      answer += arr[idx % arr.length];
    }
  
    return answer;
  }