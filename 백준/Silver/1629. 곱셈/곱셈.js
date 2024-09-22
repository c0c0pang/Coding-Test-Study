const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [A, B, C] = input[0].split(' ').map(BigInt);

const two = 2n;
const dfs = (num, target) => {
    if (target === 1n) {
        return num % C;
    }
    if (target % two === 1n) {
        let number = dfs(num, (target - 1n) / 2n) % C;
        return (number * number * num) % C;

    }
    else {
        let number = dfs(num, target / 2n) % C;
        return (number * number) % C;
    }
}
dfs(A, B);
console.log(dfs(A, B).toString());


