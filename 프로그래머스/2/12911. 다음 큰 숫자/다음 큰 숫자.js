function solution(n) {
    var answer = n;
    let check = true;
    let cnt = 0
    let result = 0;
    n.toString(2).split("").map((e)=> e === "1" ? result++ : null);
    
    while(check){
        answer++
        answer.toString(2).split("").map((e)=> e === "1" ? cnt++ : null);
        if(result === cnt){
            
            check = false;
        }
        cnt = 0
    }
    return answer;
}