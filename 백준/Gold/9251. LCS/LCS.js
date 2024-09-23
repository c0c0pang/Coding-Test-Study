const fs = require('fs');
const [A, B] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let answer = 0;
const A_LEN = A.length + 1;
const B_LEN = B.length + 1;
const LCS = Array.from({ length: A_LEN }, () => Array.from({ length: B_LEN }, () => 0));

for (let i = 1; i < A_LEN; i++) {
    for (let j = 1; j < B_LEN; j++) {
        if (A[i - 1] === B[j - 1]) {
            LCS[i][j] = LCS[i - 1][j - 1] + 1;
        }
        else {
            LCS[i][j] = Math.max(LCS[i - 1][j], LCS[i][j - 1]);
        }
        answer = Math.max(answer, LCS[i][j]);
    }
}
console.log(answer)