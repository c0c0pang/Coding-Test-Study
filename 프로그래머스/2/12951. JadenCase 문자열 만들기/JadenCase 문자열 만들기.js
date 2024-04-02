function solution(s) {
    const low = s.toLowerCase();
    var answer = low.split(" ");
    const result = answer.map((e)=>{
        if(e===""){
            return "";
        }
        const up = e[0].toUpperCase();
        let str = e.split("");
        if(str[0]===up){
            return e;
        }
        str[0] = up
        return str.join("");
    })
    return result.join(" ");
}