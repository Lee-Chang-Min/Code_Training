function solution(bandage, health, attacks) {
    const [time, healTime, bonusTime] = bandage; 
    const lastAttackTime = attacks[attacks.length -1][0]
    let curHp = health;
    let successTime = 0;


    for(i = 0; i <=lastAttackTime; i++ ){

        const attack = attacks.find((at) => at[0] === i)

        //몬스터가 공격 성공했을때
        if(attack){
            curHp -= attack[1];
            successTime = 0;
            if(curHp  <= 0) return -1
        }else{
            curHp += healTime
            successTime +=1
             //붕대 로직
            if(successTime == time){
                curHp += bonusTime
                successTime = 0;
            }
        
        }
        
        curHp = health < curHp ? health : curHp
        console.log(curHp);
    }
    
    return curHp;
}
