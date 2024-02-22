function solution(numbers) {
    var answer = -1;
    return answer;
}

let numbers = [1,2,3,4,6,7,8,0]

let arrays = new Set([0,1,2,3,4,5,6,7,8,9])

numbers.forEach(element => {
    arrays.delete(element);
});

//console.log(arrays)

if(arrays.size != 0){
    arrays.forEach(v => {
        answer += v;
    })
}