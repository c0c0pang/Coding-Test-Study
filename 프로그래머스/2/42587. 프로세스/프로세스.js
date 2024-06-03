function solution(priorities, location) {
    var answer = 0;
    const process = []
    const array = []
    const queue = []
    const target = priorities[location];
    for(let i = 0;i<priorities.length;i++){
        process.push(i);
    }
    priorities.map((e,i)=>{
        array.push([e,process[i]])
    })
    while(array.length!==0){
        let check = false;
        const v = array.shift()
        for(let j=0;j<array.length;j++){
            if(v[0]<array[j][0]){
                check = true;
                break;
            }
        }
        if(check){
            array.push(v);
        }
        else{
            answer++;
            if(v[1]===location){
                break;
            }
        }
    }
    return answer;
}