function solution(number) {
    var answer = 0;
    return answer;
}

let number =   [0, 0, 1, -1, 0]
let answer = 0;

// for(let i = 0; i < number.length; i++){
//     //console.log(number.length);
//     let count = i+1
//     while(count < number.length){
        
//         let f = number[i]+ number[count];
//         //console.log(f);
//         let R = number.slice(count+1).find((v) => {
//             if(v + f === 0){
//                 answer +=1;
//                 return -1;
//             } 
//         });
        
//         if(R === -1){ break }
//         count++;
//     }
//     console.log(answer);

// }

// for(let i=0; i<number.length; i++){
//     for(let j=0;j<number.length;j++){
//         for(let k=0;k<number.length;k++){
//             if(i !== j && j !== k && i!== k){
//                 if((number[i] + number[j] + number[k])===0) answer += 1
//             }
//         }   
//     }
// }

for(let i =0; i < number.length-2; i++){
    for(let j = i+1; j < number.length-1; j++){
        for(let k = j+1; k < number.length; k++){
              const sum = number[i] + number[j] + number[k]
            if(sum === 0) answer++
        }
    }
}

console.log(answer);