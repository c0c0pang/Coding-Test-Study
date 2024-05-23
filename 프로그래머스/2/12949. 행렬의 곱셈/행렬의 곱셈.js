function solution(arr1, arr2) {
    const arr1_length = arr1.length;
    const arr2_length = arr2.length;
    const arr2_row_length = arr2[0].length;
    var answer = Array.from(Array(arr1_length),()=>new Array());
    arr1.map((e,w)=>{
        for(let i = 0; i<arr2_row_length;i++){
            let sum = 0;
                e.map((l,z)=>{
                    sum+=l*arr2[z][i];
                })
                answer[w].push(sum)
        }
    })
    return answer;
}
//(1,4) (3,3)
//(3,2) (3,3)
//(4,1)
// [0][0] [1][0] [2][0]