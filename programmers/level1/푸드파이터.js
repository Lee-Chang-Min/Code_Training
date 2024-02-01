function solution(food) {
    var answer = '';
    return answer;
}

let answer = [];
let food = [1, 3, 4, 6];

"1223330333221"

for(let i = 1; i < food.length; i++){
    let foodCount = food[i];
    //console.log(food[f]);
    if(food[i] === 1) continue;

    if(food[i] % 2 === 1){
        foodCount = food[i] - 1 //음식의 갯수
    } 

    for(let c = 1; c <= foodCount/2 ; c++){
        answer.push(i)
    }
    
}

answer.push(0)
for()

console.log(answer);
