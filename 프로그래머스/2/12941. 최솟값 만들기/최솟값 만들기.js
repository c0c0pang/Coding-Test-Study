function solution(A,B){
    var answer = 0;
    A.sort((a,b)=>a-b);
    B.sort((a,b)=>b-a)
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    A.forEach((e,i)=>{
        answer+=e*B[i]
    })
    return answer;
}