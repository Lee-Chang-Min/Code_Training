function solution(cards1, cards2, goal) {
    var answer = '';
    return answer;
}
let F_answer = [];
let S_answer = [];
let cards1 = ["i", "drink", "water"]
let cards2 = ["want", "to"]
let goal =  ["i", "want", "to", "drink", "water"]
let result = 'Yes'
goal.map((item, idx) => {
    let a;
    if(cards1.indexOf(item) !== -1){
       a = 'F' + cards1.indexOf(item);
       cards1[a] = 0
    }else{
        a = 'S' + cards2.indexOf(item);
        cards2[a]= 0;
    }

    if(a.charAt(0) === 'F') F_answer.push(a);
    if(a.charAt(0) === 'S') S_answer.push(a);
    
})

F_answer.some((ele, idx) => {

    
    if(F_answer[idx+1] !== undefined && Number(ele.charAt(1)) + 1 !== Number(F_answer[idx+1].charAt(1))){
        result = 'No';
        return true;
    }    
    
    if(F_answer[idx+1] == undefined || ele.charAt(1) <= F_answer[idx+1].charAt(1)){
        return false;
    }else{
        result = 'No';
        return true;
    }
    
})

S_answer.some((ele, idx) => {
    if(S_answer[idx+1] !== undefined && ele.charAt(1) + 1 !== S_answer[idx+1].charAt(1)){
        result = 'No';
        return true;
    }    
    if(S_answer[idx+1] == undefined || ele.charAt(1) <= S_answer[idx+1].charAt(1)){
        return false;
    }else{
        result = 'No';
        return true;
    }
    
})


/**
 * shift로 인한 풀이
 */
function solution(cards1, cards2, goal) {

    for(const s of goal) {

        if(cards1[0] == s) {
            cards1.shift();
        } else if(cards2[0] == s) {
            cards2.shift();
        } else {
            return "No"
        }
    }

    return "Yes";
}

