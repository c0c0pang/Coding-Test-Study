function solution(wallpaper) {
    var answer = [];
    const wallpaper_bri = []
    let [x_1,y_1] = [50,50];
    let [x_2,y_2] = [-1,-1];
    wallpaper.forEach((e,i)=>{
        const arr = e.split("");
        arr.forEach((se,j)=>{
            if(se==="#"){
                x_1 = x_1>i ? (i):(x_1);
                y_1 = y_1>j ? (j):(y_1);
                x_2 = x_2<i ? (i):(x_2);
                y_2 = y_2<j ? (j):(y_2);
            }
        })
    })
    return [x_1,y_1,x_2+1,y_2+1];
}
//첫좌표 :제일 낮은걸 기준
//마지막좌표:제일 높은걸 기준 