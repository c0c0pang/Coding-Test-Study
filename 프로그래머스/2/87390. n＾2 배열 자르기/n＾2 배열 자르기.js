function solution(n, left, right) {
    var answer = Array.from({length:(right-left)+1},()=>0);
    for(let i =left;i<=right;i++){
        const v = i%n;
        answer[i-left] = v+1;
    }
    for(let i=left;i<=right;i++){
        answer[i-left] = Math.max(answer[i-left],Math.floor(i/n)+1);
    }
    
    return answer;
}
// 1234 2234 3334 4444