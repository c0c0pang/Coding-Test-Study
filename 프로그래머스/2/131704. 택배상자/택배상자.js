function solution(order) {
    var answer = 0;
    const stack = [];
    const LEN = order.length;
    let idx = 0;
    for(let i =1;i<=LEN;i++){
        if(order[idx]===i){
            answer++;
            idx++;
        }else{
            stack.push(i);
        }
        while(stack.length!==0){
            if(order[idx]!==stack[stack.length-1]) break;
            stack.pop();
            idx++;
            answer++;
        }
        
    }
    return answer;
}