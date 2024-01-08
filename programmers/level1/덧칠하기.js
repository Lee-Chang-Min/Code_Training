function solution(wall, draw, section) {
    var answer = 0;


let section = [2, 3, 6]

let paint = 0;
for (const s of section) {
    if (s <= paint) continue;
    else {
        paint = s + (m-1);
        answer++;
    }
}

return answer;
}