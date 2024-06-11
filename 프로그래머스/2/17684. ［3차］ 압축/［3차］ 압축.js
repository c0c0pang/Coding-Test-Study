function solution(msg) {
    var answer = [];
    const array = msg.split("");
    const enc = {};
    const visited = Array.from({length:array.length},()=>false);
    for(let i =1;i<=26;i++){
        const str = String.fromCharCode(i+64);
        enc[str] = i;
    }
    let w=array.shift();
    while(array.length!==0){
        let c = array.shift()
        const w_c = w+c;
        if(enc[w_c]===undefined){
            const size = Object.keys(enc).length;
            answer.push(enc[w]);
            w = c;
            enc[w_c] =size+1; 
        }
        else{
            w+=c;
        }
    }
    answer.push(enc[w])
    return answer;
}