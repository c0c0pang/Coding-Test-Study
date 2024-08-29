const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
let str = '';
let double = '';
const token = [];
const box = [' ', '<', '>', '(', ')', '|', '&'];
for (let i = 0; i < input.length; i++) {
    if (box.indexOf(input[i]) === -1) {
        str += input[i];
    }
    if (box.indexOf(input[i]) >= 0) {
        if (str !== '') {
            token.push(str);
            str = '';
        }
        if (input[i] !== ' ' && (input[i] !== '|' && input[i] !== '&')) {
            token.push(input[i]);
        }
        if (input[i] === '|' || input[i] === '&') {
            double += input[i];
        }
    }
    if (double === '||' || double === '&&') {
        token.push(double);
        double = '';
    }
}
if (str !== '') token.push(str);
console.log(token.join(' '));
