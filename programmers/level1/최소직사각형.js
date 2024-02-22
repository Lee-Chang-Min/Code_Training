function solution(sizes) {
    var answer = 0;
    return answer;
};

let sizes = [[60, 50], [30, 70], [60, 30], [80, 40]];
let 가로 = 0;
let 세로 = 0;


sizes.forEach((v) => {
    //console.log(v)
    if(v[0] < v[1]){
        v.push(v[0]);
        v.shift()
    }

    if(v[0] > 가로) 가로 = v[0]
    if(v[1] > 세로) 세로 = v[1]
});

console.log(가로 * 세로);


/**좋은 풀이 */

const rotated = sizes.map(([w, h]) => w < h ? [h, w] : [w, h]);

let maxSize = [0, 0];
rotated.forEach(([w, h]) => {
    if (w > maxSize[0]) maxSize[0] = w;
    if (h > maxSize[1]) maxSize[1] = h;
})
return maxSize[0]*maxSize[1];
