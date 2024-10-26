/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = []
    const arr = s.split('')
    while(arr.length){
        const LEN = stack.length;
        const str = arr.pop();
        if(LEN===0){
            stack.push(str)
            continue
        }
        if(stack[LEN-1]===')' && str==='('){
            stack.pop()
            continue
        }
        if(stack[LEN-1]==='}' && str==='{'){
            stack.pop()
            continue
        }
        if(stack[LEN-1]===']' && str==='['){
            stack.pop()
            continue
        }
        stack.push(str)
    }
    if(stack.length===0){
        return true
    }
    return false
};