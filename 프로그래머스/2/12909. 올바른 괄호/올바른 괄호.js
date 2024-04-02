function solution(s){
    var answer = false;
    const arr = s.split("").reverse();
    const stack = [arr.pop()];
    while(arr.length){
        const str = arr.pop();
        if(stack[stack.length-1]+str==="()"){
            stack.pop();
        }
        else{
            stack.push(str);
        }
    }
    if(stack.length===0){
        return true;
    }
    return false;
}