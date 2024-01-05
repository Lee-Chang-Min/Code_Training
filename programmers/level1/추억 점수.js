function solution(name, yearning, photo) {
    var answer = [];
    return answer;
}
function s(){
    var answer = [];

    let name = ["may", "kein", "kain", "radi"];
    let yearning =[5, 10, 1, 3];
    let photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]];
    
    for(let p of photo){
        let s_ans = 0;
        for(let n of p){
            let score = yearning[name.indexOf(n)];
            if(score !== undefined) s_ans += score; 
        }
        answer.push(s_ans);
    }
    return answer;
}

console.log(s());

/* 참고 풀이 */

function solution(name, yearning, photo) {
    return photo.map((v)=> v.reduce((a, c)=> a += yearning[name.indexOf(c)] ?? 0, 0))
}

