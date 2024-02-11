function solution(X, Y) {
    var answer = '';
    return answer;
}

let x = "12321"
let y = "42531"

yArray =  Array.from(y)

let answer = [];

for(xIdx in x){
    //console.log(xIdx);
    
    yArray.find((yValue, i) => {
        //console.log(Array.from(x)[xIdx]);
        console.log(yValue);
        
        if(Array.from(x)[xIdx] === yValue)
        {
            answer.push(yValue);
            yArray.splice(i,1);
        }
    })
}

answer = answer.reverse();
return answer.join('')