function solution(babbling) {
    var answer = 0;
    return answer;
}
var answer = 0;
let speak = ["aya", "ye", "woo", "ma"]; 

let babbling = ["ayayemaaya"];
let result = 1;


// for(b in babbling){

//     for(s of speak){
//         var pattern = s;
//         var regex = new RegExp(pattern, 'g');
//         if(babbling[b].includes(s)){           
//                 babbling[b] = babbling[b].replace(regex, '');
//         }
//     }
//     //console.log(babbling);
// }

// babbling.forEach( v => v === '' ? answer +=1 : answer )
// console.log(babbling);

for (var i=0; i < babbling.length; i++) {
    let bab = babbling[i];
    
    for (var j=0; j < speak.length; j++) {
            if(bab.includes(speak[j].repeat(2))) {
            break;
            }
        bab = bab.split(speak[j]).join(" ");
        }
    if(bab.split(" ").join("").length === 0){
        answer ++
    }
}