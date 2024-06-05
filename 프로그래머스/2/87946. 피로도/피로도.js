function solution(k, dungeons) {
    var answer = -1;
    const btk = (k,cnt,arr,visited)=>{
        answer = Math.max(answer,cnt)
        if(arr.length===cnt){
            return;
        }
        for(let i =0;i<arr.length;i++){
            if(visited[i]){
                continue;
            }
            if(k>=arr[i][0]){
                visited[i] = true;
                btk(k-arr[i][1],cnt+1,arr,visited);
                visited[i] = false;
            }
        }
    }
    const visited = Array.from({length:dungeons.length},()=>false)
    btk(k,0,dungeons,visited)
    return answer;
}
//1 2 3 4
//1 2 4 3