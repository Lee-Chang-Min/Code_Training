function solution(today, terms, privacies) {
    var answer = [];
    return answer;
}
var answer = [];


let today =  "2020.05.15"
let terms = ["A 1"]
let privacies = ["2001.01.10 A", "2001.01.10 A"]

let today1 = new Date(today);


for(let [i,p] of privacies.entries()){
    let pdate = new Date(p.split(' ')[0]);
    let ptype = p.split(' ')[1];
    
    
    let checkTerms = terms.filter((v, i) => ptype === v.split('')[0]);
    //["A 6"]
    
    let termsMonth = Number(checkTerms[0].split(' ')[1]);

    pdate.setMonth(pdate.getMonth() + termsMonth );

    if(pdate <= today1) {
        answer.push(i+1)
    }

}

console.log(answer);

"2010.01.01", ["A 12"], ["2009.12.01 A", "2001.01.01 A"]