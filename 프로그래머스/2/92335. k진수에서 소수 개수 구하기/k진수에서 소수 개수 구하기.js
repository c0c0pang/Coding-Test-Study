function solution(n, k) {
    var answer = 0;
     const array = n.toString(k).split('0');
    array.map((e)=>{
        const num = Math.sqrt(+e);
        if(e<2){
            return;
        }
        else if(e===2){
            answer++;
        }
        else{
            let check = false;
            for(let i =3;i<=num;i+=2){
                if(e%i===0){
                    check = true;
                    break;
                }
            }
            if(!check){
                answer++
            }   
        }
    })
    return answer;
}