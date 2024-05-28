function solution(cacheSize, cities) {
    var answer = 0;
    const array = [];
    for(let i = 0;i<cities.length;i++){
        let swap;
        let check = false;
        const lower = cities[i].toLowerCase();
        if(array.length===cacheSize){
            for(let j = 0;j<array.length;j++){
                if(lower===array[j]){
                    for(let z = j;z<array.length-1;z++){
                        swap = array[z+1]
                        array[z+1] = lower
                        array[z] = swap   
                    }
                    check  = true;
                    answer++;
                    break;
                }
            }
            if(!check){
                array.shift();
                array.push(lower)   
                answer+=5
            }
        }
        else{
            for(let j = 0;j<array.length;j++){
                if(lower===array[j]){
                    for(let z = j;z<array.length-1;z++){
                        swap = array[z+1]
                        array[z+1] = lower
                        array[z] = swap   
                    }
                    check  = true;
                    answer++;
                    break;
                }
            }
            if(!check){
                array.push(lower)    
                answer+=5
            }
            
        }
    }    
    if(cacheSize===0){
        return cities.length*5
    }
    return answer;
}
// 1 2 4 3 