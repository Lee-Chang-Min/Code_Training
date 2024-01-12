let keymap = ["ABCDE", "ABBCE"]
let targets = ["ABFBE"]
         
function solution(keymap, targets) {
    var answer = [];

    for(target of targets){
        let total = 0;
        let to = Array.from(target);
        for(let t of to){
            let num = [];
            console.log(t, t)
            for(k of keymap){
                let idx = Array.from(k).findIndex((idx) => idx === t)
                if(idx !== -1){
                    num.push(idx);
                }
                
            }
            console.log(num.filter(v => v === -1).length)
            if(num.length !== 0 && num.filter(v => v === -1).length !== keymap.length){
                total += Math.min(...num)+1;
            }else{
                total = -1;
                break;
            }
        }
        answer.push(total);

    }
    return answer;
}


/*
reduce와 map을 활용한 풀이 뜯어보기
*/
    const map1 = {}
    for (const items of keymap) {
        console.log(items.split(''));
        
        items.split('').map((item, index) => {
            console.log(map1[item]);
            console.log(index+1);
            console.log(map1[item] < index+1);
            
            map1[item] = (map1[item] < index+1 ? map1[item] : index+1);
            console.log(map1);
            
    })
    }

    for (const items of targets) {
        answer.push(
            items.split('').reduce(
                (cur, item) => 
                    // console.log(cur);
                    // console.log(map1[item])
                    cur += map1[item], 0
                ) || -1
        )
    }