function solution(wallpaper) {

// let firstCurse_H = wallpaper.findIndex((f) => f.includes("#"));
// let firstCurse_W = [...wallpaper[firstCurse_H]].indexOf('#');
// let lastCurse_H = wallpaper.length +1
// let lastCurse_W = 0;

// for(w of wallpaper){
//     let first = [...w].indexOf('#');
//     let last = [...w].lastIndexOf('#');

//     if()
//     if(first < firstCurse_W && first !== -1) firstCurse_W = first
//     if(last > lastCurse_W && last !== -1) lastCurse_W = last
// }
// answer = [firstCurse_H, firstCurse_W, lastCurse_H, lastCurse_W + 1];

 
let [x1, y1, x2, y2] = [wallpaper.length, wallpaper[0].length, 0, 0];
// x1 => min i
// x2 => max i
// y1 => min idx
// y2 => max idx
wallpaper.forEach((paper, i) => {
  if (paper.includes('#')) {
    x1 = Math.min(x1, i);
    y1 = Math.min(y1, paper.indexOf('#')); //파란색
    x2 = Math.max(x2, i);
    y2 = Math.max(y2, paper.lastIndexOf('#'));
  }
});
return [x1, y1, x2 + 1, y2 + 1];

}
solution();