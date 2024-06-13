function solution(word) {
    var answer = 0;
    const array = ['A','E','I','O','U'];
    const visited = Array.from({length:array.length},()=>false);
    let cnt = 0;
    const btk = (str)=>{
        if(str.length>4){
            return;
        }
        for(let i =0;i<array.length;i++){
            cnt++;
            if(word===str+array[i]){
                answer = cnt;
                return;
            }
            btk(str+array[i]);
        }
    }
    btk("");
    return answer;

}