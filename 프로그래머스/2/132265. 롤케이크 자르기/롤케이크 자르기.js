function solution(topping) {
    var answer = 0;
    const arr_1 = [];
    const arr_2 = [];
    const set_1 = new Set(); 
    const set_2 = new Set(); 
    const length = topping.length;
    for(let i=0;i<length;i++){
        set_1.add(topping[i]);
        arr_1.push(set_1.size);
    }
    topping.reverse();
    for(let i=0;i<length;i++){
        set_2.add(topping[i]);
        arr_2.push(set_2.size);
    }
    arr_2.reverse();
    for(let j=0;j<length-1;j++){
        if(arr_1[j]==arr_2[j+1]) answer++;
    }
    return answer;
}