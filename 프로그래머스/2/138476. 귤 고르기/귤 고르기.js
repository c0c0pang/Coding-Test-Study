function solution(k, tangerine) {
    var answer = 0;
    const arr = [];
    tangerine.map((e)=>{
        if(arr[e]){
            arr[e][1]+=1
        }
        else{
            arr[e]=[e,1]
        }
    });
    arr.sort((a,b)=>b[1]-a[1])
    
    for(let i=0;i<arr.length;i++){
        if(k-arr[i][1]>0){
            k-=arr[i][1];
            answer++;
        }
        else{
            answer++;
            break;
        }
    }
    
    return answer;
}
