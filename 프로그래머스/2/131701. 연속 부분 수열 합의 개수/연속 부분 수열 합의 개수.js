function solution(elements) {
    var answer = 0;
    const set = new Set()
    const length = elements.length;
    for(let i=0;i<length;i++){
        let sum = 0;
        for(let j=i;j<length+i;j++){
            sum+=elements[j%length]
            set.add(sum)
        }
    }
    return set.size;
}
//4,9
