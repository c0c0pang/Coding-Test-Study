function solution(bandage, health, attacks) {
    var answer = 0;
    let suc = 0; //연속성공
    const SIZE = attacks.length-1;
    const last = attacks[SIZE][0];
    const obj = new Map();
    const H = health;
    attacks.map((e)=>{
        obj.set(e[0],e[1])
    })
    for(let i=0; i<=last; i++){
        const attack = obj.get(i);
        if(health<=0){
            break;
        }
        if(attack){
            suc = 0;
            health-=attack;
        }
        else{
            suc+=1;
            if(bandage[0]===suc){
                if(health+bandage[1]+bandage[2]<=H){
                    health+=bandage[1]+bandage[2];
                }else{
                    health=H
                }
                suc = 0;
            }
            else{
                if(health+bandage[1]<=H){
                    health+=bandage[1];   
                }
                else{
                    health=H
                }
            }
        }
        
    }
    if(health<=0){
        return -1;
    }
    else{
        return health;
    }
}