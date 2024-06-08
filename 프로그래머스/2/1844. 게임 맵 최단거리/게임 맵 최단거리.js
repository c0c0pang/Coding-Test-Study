
function solution(maps) {
    const in_range = (x,y,n,m) =>{
        return x>n || x<0 || y>m||y<0;
    }
    var answer = -1;
    const [dx,dy] = [[-1,1,0,0],[0,0,-1,1]];
    const visited = Array.from({length:maps.length},()=>{
        return Array.from({length:maps[0].length},()=>false);
    })
    const array = [];
    array.push([0,0,0]);
    while(array.length!==0){
        const v = array.shift();
        if(v[0]===maps.length-1 && v[1]===maps[0].length-1){
            answer = v[2]+1
            break;
        }
        for(let i =0;i<4;i++){
            const [nx,ny] = [v[0]+dx[i],v[1]+dy[i]];
            if(in_range(nx,ny,maps.length-1,maps[0].length-1)){
                continue;
            }
            if(maps[nx][ny]===0){
                continue;
            }
            if(visited[nx][ny]){
                continue;
            }
            array.push([nx,ny,v[2]+1]);
            visited[nx][ny]=true;
        }
        
    }
    return answer;
}