function solution(n) {
    var answer = 0;
    const dp = Array.from({length:n},()=>0);
    for(let i = 0;i<n;i++){
        if(i===0){
            dp[i] = 1;
            continue;
        }
        if(i===1){
            dp[i] = 2;
            continue;
        }
        dp[i] = (dp[i-2]%1000000007 + dp[i-1]%1000000007)%1000000007;
    }
    answer = dp[n-1];
    return answer;
}