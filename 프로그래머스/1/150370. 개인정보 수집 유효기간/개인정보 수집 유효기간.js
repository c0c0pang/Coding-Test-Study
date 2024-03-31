function solution(today, terms, privacies) {
    var answer = [];
    const [year,month,day] = today.split(".");
    let cnt = 1;
    privacies.forEach((p)=>{
        const [p_1,p_2] = p.split(" ");//t_1년도,t_2 약관
        terms.forEach((t)=>{
            let [t_1,t_2] = t.split(" ");//t_1약관,t_2 달
            let [y,m,d] = p_1.split(".");
            t_2 = +t_2;
            const l_m = t_2%12;
            const l_y = Math.floor(t_2/12);
            if(t_1!==p_2){
                return;
            }
            y=+y+l_y;
            m=+m+l_m;
            d=+d;
            if(m>12){
                const d_m = m%12;
                const d_y = Math.floor(m/12);
                y += d_y
                m = d_m === 0 ? (1):(d_m);
                if(d-1===0){
                    d=28
                    m = m-1 ===0 ? (12):(m-1)
                }
                else{
                    d-=1
                }
            }
            else{
                if(d-1===0){
                    d=28
                    m = m-1 ===0 ? (12):(m-1)
                }
                else{
                    d-=1
                }   
            }
            if(m<10){
                m = `0${m}`
            }
            if(d<10){
                d = `0${d}`
            }
            const result = [y,m,d].join(".")
            if(today>result){
                answer.push(cnt);
            }
        })
        cnt+=1
    })
    return answer;
}