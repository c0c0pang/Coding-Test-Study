function solution(numbers) {
    var answer = 0;
    const len = numbers.length;
    const set = new Set();
    const ans = Array.from({length:len},()=>'');
    const arr = numbers.split('');
    const visited = Array.from({length:len},()=>false);
    const dfs = (cnt,target) =>{
        if(target===cnt){
            const num = ans.join('');
            set.add(Number(num));
            return;
        }
        for(let i =0;i<len;i++){
            if(visited[i]) continue;
            ans[cnt] = arr[i];
            visited[i] = true;
            dfs(cnt+1,target);
            visited[i] = false;
        }
    }
    for(let i=1;i<=len;i++){
        dfs(0,i);
    }
    const result = Array.from(set);
    const max_num = Math.max(...result);
    const check = Array.from({length:max_num+1},()=>true);
    const era = (n)=>{
        for(let i=2;i<Math.sqrt(n)+1;i++){
            if(check[i]){
                let j=2;
                while(i*j<=n){
                    check[i*j] = false;
                    j+=1;
                }
            }
        }
    }
    era(max_num);
    result.map((e)=>{
        if(e>1 && check[e]) answer++;
    })
    return answer;
}