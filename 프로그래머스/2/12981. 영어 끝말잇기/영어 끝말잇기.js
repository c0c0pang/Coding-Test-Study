function solution(n, words) {
    var answer = [];
    let num = 1;
    let turn = 1;
    let check = true;
    let obj = {};
    for(let i =0;i<words.length-1;i++){
        if(num>n){
            turn++;
            num=1;
        }
        if(words[i].slice(-1)===words[i+1].slice(0,1)){
            obj[words[i]]=i;
            if(obj[words[i+1]]>-1){
                num++;
                if(num>n){
                    turn++;
                    num=1;
                }
                check = false
                break;
            }
            num++;
        }
        else{
            num++;
            if(num>n){
                turn++;
                num=1;
            }
            check = false
            break;
        }

    }
    if(check){
        return [0,0];
    }

    return [num,turn];
}