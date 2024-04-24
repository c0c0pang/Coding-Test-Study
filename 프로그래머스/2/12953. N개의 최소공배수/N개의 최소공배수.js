function solution(arr) {
    var answer = 0;
    let num = arr[arr.length-1];
    let cnt = 1;
    let check = 0;
    let mul = 0
    while(check!==arr.length){
        mul=cnt*num;
        check = 0;
        arr.forEach((e)=>{
            if(Number.isInteger(mul/e)){
                check+=1
            }
        })
        cnt++;
    }
    return mul;
}
