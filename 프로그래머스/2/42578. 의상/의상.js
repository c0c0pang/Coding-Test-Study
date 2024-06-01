function solution(clothes) {
    const obj = {}
    const array = []
    var answer = 1;
    clothes.map((e)=>{
        if(obj[e[1]]!==undefined){
            obj[e[1]] = [...obj[e[1]],e[0]]
        }
        else{
            obj[e[1]] = [e[0]]
        }
        
    })
    const size = Object.keys(obj).length;
    for(i in obj){
        array.push(obj[i].length);
    }
    for(let j = 0;j<array.length;j++){
        answer*=(array[j]+1)
    }
    return answer-1;
}