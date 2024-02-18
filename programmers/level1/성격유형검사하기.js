function solution(survey, choices) {
    var answer = '';
    return answer;
}

let survey = ["AN", "CF", "MJ", "RT", "NA"];
let choices = 	[5, 3, 2, 7, 5];

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
    switch(choices){
        case 1:
            array[0] = 3;
        break;
        case 2:
            array[0] = 2;
        break;
        case 3:
            array[0] = 1;
        break;
        case 4:
        break;
        case 5:
            array[1] = 1;
        break;
        case 6:
            array[1] = 2;
        break;
        case 7:
            array[1] = 3;
        break;

    }
    return array;
}

for(s in survey){
    console.log(score(survey[s], choices[s])) 

}