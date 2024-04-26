function solution(n) {
    var answer = 0;
    let n1 = 0;
    let n2 = 1;
    let sum = 0;
    while(answer!==n){
        sum = (n1+n2)%1234567;
        n1 = n2;
        n2 = sum;
        answer++;
    }
    return sum;
}