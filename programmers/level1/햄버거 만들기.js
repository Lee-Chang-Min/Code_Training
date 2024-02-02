function solution(ingredient) {
    var answer = 0;
    return answer;
}

var answer = 0;
//let ingredient = [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
//let ingredient = 	[2, 1, 1, 2, 3, 1, 2, 3, 1]
let ingredient =  [1,2,1,2,3,1,3,1,2,3,1,2,3,1]

// while(ingredient.length > 4){

//     for(let idx = 0; idx<ingredient.length; idx++){
//         if(ingredient[idx] === 1){
//             if(ingredient[idx+1] === 2 && ingredient[idx+2] === 3 && ingredient[idx+3] === 1){
//                 ingredient.splice(idx, 4)
//                 answer += 1;
//             }
//         }
//     }

//     if(answer == 0) break;
// }

// 시간초과

let str = ingredient.join('');

while(str.includes('1231')){
    let t = str.length
    str = str.replaceAll('1231', '');
    answer += ((t  -  str.length) / 4);
}


console.log(answer);




// 입력값 〉 [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
// 기댓값 〉 5