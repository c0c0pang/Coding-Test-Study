function solution(s) {
    var answer;
    let befor = 0;
    let after = 0;
    let binary = s.split("");
    let cnt_a = 0;
    let cnt_b = 0;
    let cnt = 0;
    while(binary.length !==1){
        binary.map((e)=> e === "1" ? (cnt_a++):(cnt_b++));
        binary = cnt_a.toString(2);
        binary = binary.split("");
        befor+=1;
        after+=cnt_b;
        cnt_b=0
        cnt_a=0
    }
    var answer = [befor,after];
    return answer;
}