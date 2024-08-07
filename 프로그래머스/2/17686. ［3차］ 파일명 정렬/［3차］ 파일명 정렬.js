function solution(files) {
    var answer = [];
    const array = [];
    files.map((e)=>{
        const str = e.split('');
        let H_V = false;
        let N_V = false;
        let T_V = false;
        const fileName = {
            HADE:'',
            NUMBER:'',
            TAIL:'',
        }
        for(let i =0;i<str.length;i++){
            const code = str[i].charCodeAt();
            if(code>=48 && code<=57 && !T_V){
                fileName.NUMBER+=str[i];
                H_V = true;
                N_V = true;
                continue;
            }
            if(H_V && N_V){
                fileName.TAIL+=str[i];
                T_V = true;
            }
            if(!H_V){
                fileName.HADE+=str[i];
            }
        }
        array.push([fileName.HADE,fileName.NUMBER,fileName.TAIL]);
    })
    array.sort((a,b)=>{
        if(a[0].toUpperCase()===b[0].toUpperCase()){
            return +b[1] > +a[1] ? -1:1;
        }
        else{
            return b[0].toUpperCase()>a[0].toUpperCase() ? -1:1;
        }
    })
    answer = array.map((e)=>{
        return e.join("");
    })
    return answer;
}