const stack = (target) =>{
    const arr = new Array();
    let cnt = 0;
    arr.push(target[0]);
    for(let i =1;i<target.length;i++){
        if(arr[arr.length-1]+target[i]==='[]'
           ||arr[arr.length-1]+target[i]==='{}'
           ||arr[arr.length-1]+target[i]==='()')
        {
            arr.pop()
        }
        else{
            arr.push(target[i])
        }
    }
    if(arr.length){
        return false;
    }
    return true;
}
function solution(s) {
    var answer = 0;
    const arr = s.split("");
    const length = arr.length;
    for(let i = 0;i<length;i++){
        if(stack(arr)){
            answer+=1;
        }
        const puz = arr.splice(0,1);
        arr.push(puz[0]);
        
    }
    return answer;
}