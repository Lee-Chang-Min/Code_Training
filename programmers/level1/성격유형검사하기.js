function solution(survey, choices) {
    var answer = '';
    return answer;
}

let survey = ["AN", "CF", "MJ", "RT", "NA"];
let choices = 	[5, 3, 2, 7, 5];
let answer = '';

let mbti = {
    1: {
        R: 0,
        T: 0,
    },
    2: {
        C: 0,
        F: 0,
    },
    3: {
        J: 0,
        M: 0,
    },
    4:{
        A: 0,
        N: 0,
    }
}


function score(survey, choices){
    let array = survey.split('')
    let result = [];
    switch(choices){
        case 1:
            result.push(array[0],3);
            break;
        case 2:
            result.push(array[0],2);
            break;
        case 3:
            result.push(array[0],1);
            break;
        case 4:
            break;
        case 5:
            result.push(array[1],1);
            break;
        case 6:
            result.push(array[1],2);
            break;
        case 7:
            result.push(array[1],3);
            break;

    }
    return result;
}

for(s in survey){

    let result = score(survey[s], choices[s])
    
    for(let i = 1 ; i <= 4; i++){
        if(mbti[i][result[0]] != undefined){
            mbti[i][result[0]] += result[1];
        }
    }

}

//console.log(mbti);

for(let i = 1 ; i <= 4; i++){
    let keys = Object.keys(mbti[i])
    // let f_key = keys[0];
    // let s_key = keys[1];

    if(mbti[i][keys[0]] >= mbti[i][keys[1]]){
        answer += keys[0]
    }else{
        answer += keys[1]
    }
}

console.log(answer);