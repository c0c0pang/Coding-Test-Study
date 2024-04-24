function solution(brown, yellow) {
    var answer = [];
    let column = 2;
    let row = brown/2;
    let result = -1;
    while(result!==0){
        column++;
        row--;
        let mul = row*column;
        result = mul - brown - yellow;
        
    }
    return [row,column];
}