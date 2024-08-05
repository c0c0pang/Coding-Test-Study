function solution(fees, records) {
    var answer = [];
    const [DH,DF,UH,UF] = fees;
    const obj = {};
    const array = [];
    const DEF = (23*60)+59;
    records.map((e)=>{
        const [T,N,V] = e.split(" ");
        const [H,M] = T.split(":");
        const time = (+H)*60 + (+M);
        if(obj[N]===undefined){
            obj[N] = -time;
        }
        else{
            if(V==='IN'){
                obj[N] -= time;
            }
            else{
                obj[N] += time;
            }
        }
    })
    for(let j in obj){
        let result = DF;
        if(obj[j]<=0){
            obj[j]+=DEF;
        }
        if(obj[j]>DH){
            result = DF + Math.ceil((obj[j]-DH)/UH) * UF;
        }
        array.push([j,result]);
    }
    array.sort((a,b)=>a[0]-b[0]);
    array.map((e)=>{
        answer.push(e[1]);
    })
    return answer;
}