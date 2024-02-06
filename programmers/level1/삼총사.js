function solution(number) {
    var answer = 0;
    return answer;
}

let number =  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0];
let answer = 10;

for(let i = 0; i < number.length; i++){
    //console.log(number.length);
    let count = i+1
    while(count < number.length){
        
        let f = number[i]+ number[count];
        console.log(f);
        let R = number.slice(count+1).find((v) => {
            if(v + f === 0){
                answer +=1;
                return -1;
            } 
        });
        
        if(R === -1){ break }
        count++;
    }
    console.log(answer);

}

console.log(answer);


// [-2,2,-1,1,1,0,2] 

6
3
1
