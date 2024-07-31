function solution(dirs) {
    const in_range = (nx,ny)=>{
    return nx>5 || nx<-5 || ny>5 || ny<-5;
    }
    var answer = 0;
    const array = dirs.split("");
    const set = new Set();
    let x = 0;
    let y = 0;
    const command = {
        U:[-1,0],
        D:[1,0],
        L:[0,-1],
        R:[0,1],
        
    }
    array.map((e)=>{
        const [cx,cy] = command[e];            
        const nx = cx+x;
        const ny = cy+y;
        if(!in_range(nx,ny)){
            const comb = [cx*0.5+x,cy*0.5+y].join(" ");
            set.add(comb);
            x = nx;
            y = ny;
        }
    })
    return set.size;
}