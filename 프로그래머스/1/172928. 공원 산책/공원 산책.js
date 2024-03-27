const in_range=(x,y,c,r)=>{
    return x<0 || x>=c || y<0 || y>=r
}
function solution(park, routes) {
    let start;
    const stop = [];
    const cou = park.length // 행
    const row = park[0].length //열
    park.map((e,i)=>{
        for(let z=0;z<row;z++){
            if(e[z]==='S'){
                start = [i,z]
            }
            if(e[z]==='X'){
                stop.push([i,z])
            }
        }
    })
    routes.map((e)=>{
        let [m,n] = e.split(" ");
        let check = true;
        let x = start[0];
        let y = start[1];
        n = +n;
        if(m==='N'){
            let check = true;
            if(in_range(x-n,y,cou,row)){
                return;
            }
            for(let i=1;i<=n;i++){
                for(const j of stop){
                    if(x-i===j[0]&&y===j[1]){
                        check=false;
                        break;
                    }
                }
                if(!check){
                    break;
                }
            }
            if(check){
                start[0]-=n;
            }
        }
        if(m==='S'){
            let check = true;
            if(in_range(x+n,y,cou,row)){
                return;
            }
            for(let i=1;i<=n;i++){
                for(const j of stop){
                    if(x+i===j[0]&&y===j[1]){
                        check=false;
                        break;
                    }
                }
                if(!check){
                    break;
                }
            }
            if(check){
                start[0]+=n;
            }
        }
        if(m==='W'){
            let check = true;
            if(in_range(x,y-n,cou,row)){
                return;
            }
            for(let i=1;i<=n;i++){
                for(const j of stop){
                    if(x===j[0]&&y-i===j[1]){
                        check=false;
                        break;
                    }
                }
                if(!check){
                    break;
                }
            }
            if(check){
                start[1]-=n;
            }
        }
        if(m==='E'){
            let check = true;
            if(in_range(x,y+n,cou,row)){
                return;
            }
            for(let i=1;i<=n;i++){
                for(const j of stop){
                    if(x===j[0]&&y+i===j[1]){
                        check=false;
                        break;
                    }
                }
                if(!check){
                    break;
                }
            }
            if(check){
                start[1]+=n;
            }
        }
        
    })
    return start;
}