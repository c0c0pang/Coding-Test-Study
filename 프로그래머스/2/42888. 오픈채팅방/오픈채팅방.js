function solution(record) {
    const obj = {};
    let idx = 0;
    record.map((e)=>{
        const [state,id,name] = e.split(" ");
        if(obj[id]===undefined){
            obj[id]={
                idx:[],
                name:''
            }
        }
        
        const s = obj[id].idx;
        if(state==='Enter'){
            obj[id] = {
                idx:[...s,[idx++,state]],
                name:name
            };
            // answer.push(`${name}님이 들어왔습니다.`);
        }
        if(state==='Leave'){
            // answer.push(`${obj[id]}님이 나갔습니다.`);
            s.push([idx++,state])
        }
        if(state==='Change'){
            obj[id].name = name;
        }
    })
    
    var answer = Array.from({length:idx});
    for(let i in obj){
        const order = obj[i].idx;
        const name = obj[i].name;
        order.map((e)=>{
            if(e[1]==='Enter'){
                answer[e[0]] = `${name}님이 들어왔습니다.`;
            }
            else{
                answer[e[0]] = `${name}님이 나갔습니다.`;
            }
        })
    }
    return answer;
}