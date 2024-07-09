
function solution(land) {
    var answer = 0;
    const new_arr = [].concat(...land);
    const length = new_arr.length;
    const dp = Array.from({length:length},()=>0);
    for(let i=0;i<4;i++){
        dp[i] = new_arr[i];
    }
    for(let i=4;i<length;i++){
        const s = Math.floor(i/4);
        for(let j=(s-1)*4;j<s*4;j++){
            if(i-j==4) continue;
            dp[i] = Math.max(new_arr[j]+new_arr[i],dp[i]);
        }
        new_arr[i] = dp[i];
    }
    dp.sort((a,b)=>{
        return +a - (+b);
    });
    answer = dp[dp.length-1];
    return answer;
}