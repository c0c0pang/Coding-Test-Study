function solution(s)
{
    var answer = -1;
    const box = s.split("");
    const stack = new Array();
    stack.push(box.pop());
    while(box.length){
        const item = box.pop();
        if(stack[stack.length-1]===item){
            stack.pop()
        }
        else{
            stack.push(item)
        }
    }
    if(stack.length===0){
        return 1;
    }
    return 0;
}