function solution(s) {
    var answer = [];
    let str ='';
    let cnt =0;
    const result = []
    for(let i =1;i<s.length-1;i++){
        if(s[i]==='}'){
            answer.push([str,cnt]);
            cnt = 0;
            str=''
            continue;
        }
        if(s[i]===','&& s[i-1]!=='}'){
            cnt++;
            str+=',';
            continue;
        }
        if(s[i]!=='{' && s[i]!==','){
            str+=s[i];
        }
    }
    answer.sort((a,b)=>a[1]-b[1]);
    answer.map((e)=>{
        e[0].split(",")
            .map((l)=>{
            if(result.indexOf(+l)===-1){
                result.push(+l)
            }
        })
    })
    return result;
}