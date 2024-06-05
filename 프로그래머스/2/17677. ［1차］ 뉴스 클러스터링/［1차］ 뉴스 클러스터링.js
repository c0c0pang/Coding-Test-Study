function solution(str1, str2) {
    const SIZE = 65536;
    const in_range = (str) =>{
        return str.charCodeAt()>=97 &&str.charCodeAt()<=122;
    }
    var answer = 0;
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    let union = 0;
    let inter = 0;
    const new_str1 = {};
    const new_str2 = {};
    const arr_1 = [];
    const arr_2 = [];
    for(let i =0;i<str1.length-1;i++){
        if(in_range(str1[i]) && in_range(str1[i+1])){
            const result = str1[i]+str1[i+1];
            arr_1.push(result);
            if(new_str1[result]===undefined){
                new_str1[result]=1;
            }
            else{
                new_str1[result]+=1;
            }
        }
    }
    for(let j =0;j<str2.length-1;j++){
        if(in_range(str2[j]) && in_range(str2[j+1])){
            const result = str2[j]+str2[j+1];
            arr_2.push(result);
            if(new_str2[result]===undefined){
                new_str2[result]=1;
            }
            else{
                new_str2[result]+=1;
            }
        }
    }
    for(l in new_str1){
        if(new_str2[l]===undefined){
            new_str2[l] = new_str1[l];
            continue;
        }
        inter+=Math.min(new_str2[l],new_str1[l])
        
        if(new_str2[l]<new_str1[l]){
            new_str2[l] = new_str1[l]
        }
    }
    for(q in new_str2){
        union+=new_str2[q];
    }
    if(union ===0 &&inter===0){
        return SIZE;
    }
    answer = Math.floor((inter/union)*SIZE)
    return answer;
}