function solution(park, routes) {

    const parkHigh = park.length;
    const parkWidth = park[0].length;

    const directions = {
        E: [0, 1],
        W: [0, -1],
        S: [1, 0],
        N: [-1, 0],
    };


    let row = park.findIndex((s) => s.includes("S"));
    let col = park[row].indexOf("S");
    let start = [row, col] 


    for (const route of routes) {
        const [dir, distanceStr] = route.split(" ");
        let distance = parseInt(distanceStr);
        let [nx, ny] = start;

        // 주어진 걸음수 만큼 한칸씩 이동
        let step = 0;
        while (step < distance) {
        nx += directions[dir][0];
        ny += directions[dir][1];
        // 만약 밖에 나가게 되거나 X를 만나게 된다면 종료
        if (nx < 0 || parkHigh <= nx || ny < 0 || parkWidth <= ny || park[nx][ny] === "X") break;
        step++;
        }
        // 원하는 걸음수를 채우면 start는 마지막 위치로 바꿈
        if (step === distance) start = [nx, ny];
    }
    
  return start;

}