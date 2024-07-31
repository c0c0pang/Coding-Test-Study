function solution(skill, skill_trees) {
    const array = skill.split("");
    const ans = [];
    const SIZE = array.length;
    const obj = {};
    var answer = 0;
    let s = ""
    for(let i =0;i<SIZE;i++){
        obj[array[i]] = i+1;
        s+=array[i];
        ans.push(s);
    }
    skill_trees.map((e)=>{
        let result = "";
        e.split("").map((x)=>{
            if(obj[x]){
                result+=x;
            }
        })
        if(ans.indexOf(result)>-1)answer++;
        if(result==="") answer++;
    })
    return answer;
}