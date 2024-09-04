function solution(numbers) {
    var answer = '';
    const ans = [];
    const SIZE = numbers.length;
    const arr = numbers
        .map((e)=>String(e))
        .map((l)=>{
            let cnt = 0;
            let str = l;
            while(cnt!=2){
                str+=l;
                cnt++;
            }
            if(str.length>4){
                return [str.substring(0,4),l];
            }
            return [str,l];
    })
    const result = arr.sort().reverse().map((e)=>e[1]);
    answer = result.join('')
    if(answer==0){
        return '0';
    }
    return answer;
}