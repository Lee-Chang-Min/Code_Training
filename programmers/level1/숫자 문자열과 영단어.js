function solution(s) {
    var answer = 0;
    return answer;
}

let numberObject= {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

let s = "one4seveneight"

for(n in numberObject){
    s = s.replaceAll(numberObject[n],n)
    
}
