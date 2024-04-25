function solution(people, limit) {
    var answer = 0;
    let start = 0;
    let last = people.length-1;
    people.sort((a,b)=>a-b);
    while(start<=last){
        if(people[start]+people[last]<=limit){
            start++;
            last--;
            answer++;
        }
        else{
            last--;
            answer++;
        }
    }
    return answer;
}