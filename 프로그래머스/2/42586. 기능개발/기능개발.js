function solution(progresses, speeds) {
    var answer = [];
    const array = []
    let date = 0;
    let cnt = 0;
    for(let i = 0;i<progresses.length;i++){
        let new_date = 0;
        let sum = progresses[i]
        while(sum<100){
            sum+=speeds[i];
            new_date+=1;
        }
        if(new_date>date){
            date = new_date;
            array.push(1)
        }
        else{
            array[array.length-1]+=1
        }
    }
    return array;
}