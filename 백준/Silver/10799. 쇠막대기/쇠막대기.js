const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const array = input.split('');
const stack = [];
let answer = 0;
while (array.length) {
    const value = array.pop();
    const len = array.length;
    if (value === ')') {
        stack.push(len);
        continue;
    }
    const p = stack.pop();
    if (p - len === 1 && stack.length > 0) {
        answer += (stack.length);
        continue
    };
    if (p - len !== 1) answer++;
}
console.log(answer);