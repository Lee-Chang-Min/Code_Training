function solution(today, terms, privacies) {
    var answer = [];
    return answer;
}
var answer = [];


let today = "2022.05.19"
let terms = ["A 6", "B 12", "C 3"]
let privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

let today1 = new Date(today);
for(let p of privacies){
    let pdate = new Date(p.split(' ')[0]);
    let ptype = p.split(' ')[1];
    
    
    let checkTerms = terms.filter((v, i) => ptype === v.split('')[0]);
    //["A 6"]

    let termsMonth = Number(checkTerms[0].split(' ')[1]);

    if(pdate.getMonth() + termsMonth > 12 ){

        let year = today.getFullYear() +(pdate.getMonth() + termsMonth % 12)
        Number(pdate.split('.')[0]) + Number(pdate.split('.')[1]) + Number(checkTerms[0].split(' ')[1]) % 12
    }

}
