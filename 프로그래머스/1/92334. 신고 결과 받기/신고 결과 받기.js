function solution(id_list, report, k) {
    const set_report = new Set(report);
    const obj_report = {}
    const obj_list = {}
    const obj = {}
    id_list.map((e)=>{
        obj_report[e]=0
        obj_list[e]=[]
        obj[e]=0
    })
    for(const i of set_report){
        const [v1,v2] = i.split(" ");
        obj_report[v2]++
        obj_list[v1].push(v2)
    }
    id_list.map((e)=>{
        if(obj_report[e]>=k){
            for(const i in obj_list){
                if(obj_list[i].includes(e)){
                    obj[i]++
                }
            }
        }
    })
    return Object.values(obj);
}