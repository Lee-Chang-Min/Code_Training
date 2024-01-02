function solution(players, callings) {
    var answer = [];
    
    let pMap = new Map();
    
    for(let i = 0; i<players.length; i++){
        pMap.set(players[i], i);
    }
    
    for(c of callings){
        
        const idx = pMap.get(c);
        const prev = players[idx-1];
        
        pMap.set(c, idx-1);
        pMap.set(prev, idx);
        players[idx] = prev;
        players[idx-1] = c;
    }

    answer = players    
    return answer;
}

