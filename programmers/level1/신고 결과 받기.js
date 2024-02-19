function solution(id_list, report, k) {
    var answer = [];
    return answer;
}


//나의 풀이
let id_list = ["muzi", "frodo", "apeach", "neo"]
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
let k = 2;

//중복제거 
let reports =  [...new Set(report)];

let warn_idlist = new Map()

for(r of reports){
    warn_idlist.set(r.split(' ')[1], (warn_idlist.get(r.split(' ')[1]) || 0)+1)
}
warn_idlist.forEach((v, key) => {
    if(k > v){
        warn_idlist.delete(key)
    }
})
// //신고당한 횟수
// console.log(warn_idlist);

//console.log(warn_idlist.key('frodo'));

//누가 신고를 하였는데
let wholist = new Map()
for(r of reports){
    let key = r.split(' ')[0];
    let value = wholist.get(r.split(' ')[0]) || []
    value.push(r.split(' ')[1])
    wholist.set(key, value)
}

//console.log(wholist);

for(id of id_list){
    let count = 0;
    let result = wholist.get(id) || []

    result.forEach((v) => {
        if(warn_idlist.has(v)) count++; 
    })
    answer.push(count);
}

console.log(answer);


//새로운 풀이

//let reports = [...new Set(report)].map(a=>{return a.split(' ')});
console.log(reports);
let counts = new Map();
for (const bad of reports){
    counts.set(bad[1],counts.get(bad[1])+1||1)
}

// console.log(counts);

let good = new Map();
for(const report of reports){
    if(counts.get(report[1])>=k){
        good.set(report[0],good.get(report[0])+1||1)
    }
}
console.log('good',good);

let answer = id_list.map(a=>good.get(a)||0)

console.log(answer);