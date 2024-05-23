function solution(citations) {
    var answer = 0;
    citations.sort();
    const length = citations[citations.length-1];
    for(let i = 0;i<=length;i++){
        let cnt = 0;
        citations.map((e)=>{
            if(i<e){
                cnt++;
            }
        })
        // console.log(i,cnt)
        if(i===cnt){
            answer = cnt
        }
    }
    return answer;
}