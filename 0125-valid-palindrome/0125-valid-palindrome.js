/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let str = s.toLowerCase()
    const arr =[]
    for(let i =0;i<str.length;i++){
        const code = str[i].charCodeAt();
        if(code>47 && code<58){
            arr.push(str[i])
        }
        if(code>96 && code<122){
            arr.push(str[i])
        }
    }
    const result = arr.join("");
    const result_reverse = arr.reverse().join("")
    if(result===result_reverse) return true
    return false
};