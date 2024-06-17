function solution(numbers) {
    var answer = Array.from({length:numbers.length},()=>-1);
    const stack =[];
    const SIZE = numbers.length-1;
    numbers.reverse();
    stack.push([SIZE,numbers[SIZE]]);
    for(let i = SIZE-1; i>-1;i--){
        while(stack.length!==0){
            if(stack[stack.length-1][1]<numbers[i]){
                const v = stack.pop();
                answer[v[0]] = numbers[i];
            }
            else{
                break;
            }
        }
        stack.push([i,numbers[i]]);
    }
    answer.reverse();
    return answer;
}