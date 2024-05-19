function solution(want, number, discount) {
    var answer = 0;
    for(let i=0;i<discount.length;i++){
        const obj = {}
        let cnt = 0
        for(let i =0;i<want.length;i++){
            obj[want[i]] = 0
        }
        if(i+10>discount.length){
            break;
        }
        for(let j =i;j<i+10;j++){
            obj[discount[j]]+=1;
        }
        for(let z = 0;z<want.length;z++){
            if(obj[want[z]]!==number[z]){
                break;
            }
            cnt++;
        }
        if(cnt===want.length){
            answer++;
        }
    }
    return answer;
}