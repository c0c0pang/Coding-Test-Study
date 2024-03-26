function solution(n)
{
    var answer = 0;
    answer = (n+"").split("")
    let sum_num = 0
    for(let i = 0;i<answer.length;i++){
        sum_num+=+answer[i];
    }
    return sum_num;
}