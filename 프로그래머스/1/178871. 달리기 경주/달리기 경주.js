function solution(players, callings) {
    var answer = [];
    const obj_1=new Map()
    const obj_2=new Map()
    players.map((e,i)=>{
        obj_1.set(i,e);
        obj_2.set(e,i);
    })
    callings.map((e)=>{
        const v_1 = obj_2.get(e);//call num
        const get = obj_1.get(v_1-1)// change name
        const v_2 = obj_2.get(get);//call num
        obj_2.set(e,v_2)
        obj_2.set(get,v_1)
        obj_1.set(v_2,e)
        obj_1.set(v_1,get)
    })
    answer=[...obj_2].sort((a,b)=>a[1]-b[1])
    const last = []
    for(const i of answer){
        last.push(i[0])
    }
    return last;
}