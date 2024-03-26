function solution(friends, gifts) {
    const obj_1 = {}
    const obj_2 = {}
    const obj_3 = {}
    const visited = {}
    friends.map((name)=>{
        obj_1[name]={}
        obj_2[name]=0
        obj_3[name]=0
        visited[name]=false
        friends.map((e)=>{
            if(e!==name){
                obj_1[name][e]=0   
            }
        })
    })
    gifts.map((e)=>{
        [i,o] = e.split(" ")
        
        obj_1[i][o]++
        
        obj_2[i]++
        obj_2[o]--
    })
    for(const i in obj_1){
        for(const j in obj_1[i]){
            if(visited[j]){
                continue
            }
            if(obj_1[i][j]>obj_1[j][i]){
                obj_3[i]++
            }
            else if(obj_1[i][j]<obj_1[j][i]){
                obj_3[j]++
            }
            else{
                if(obj_2[i]>obj_2[j]){
                    obj_3[i]++
                }
                else if(obj_2[i]<obj_2[j]){
                    obj_3[j]++
                }
            }
        }
        visited[i] = true
    }
    let v = -1
    for(const i in obj_3){
        if(v<obj_3[i]){
            v = obj_3[i]
        }
    }
    return v;
}