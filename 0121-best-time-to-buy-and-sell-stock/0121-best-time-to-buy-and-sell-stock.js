/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    const LEN = prices.length;
    let start = 0;
    let end = 0;
    let answer = 0;
    while(end<LEN){
        const cost = prices[end]-prices[start];
        if(cost>=0){
            end+=1;
            answer = Math.max(answer,cost);
        }
        else{
            start+=1;
        }
    }
    return answer;
};

//prices 배열의 인덱스는 날짜를 의미
//최고의 매수 타이밍을 선택
//start,end 변수를 이용하여 투 포인터 사용
//초기 설정은 s,e =0,0이며 e-s 연산 시 양수가 나오면 s를 유지고 e +1 이동
//음수가 나오면 s,e +1 이동
//종료 시점은 s와 e가 LEN에 도달할 때이다.
