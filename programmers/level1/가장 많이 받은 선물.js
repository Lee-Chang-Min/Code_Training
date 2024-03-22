function solution(friends, gifts) {
    var answer = 0;
    return answer;
}

let friends = ["muzi", "ryan", "frodo", "neo"];
let gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
let result = 2


let 지수Object = {}
for(f of friends){
    지수Object[f] = [0, 0, 0];
}

for(g of gifts){
    let gArray = g.split(' ');
    // if(지수Object.hasOwnProperty(g[0]) == false){
    // }

    //console.log(gArray[1]);
    지수Object[gArray[0]][0]++
    지수Object[gArray[1]][1]++

}

console.log(지수Object);