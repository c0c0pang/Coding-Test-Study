const fs = require('fs');
const [nums, word] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');


const [n, m] = nums.trim().split(" ");
const word_arr = word.trim().split(" ").sort();
const vowel = ['a', 'e', 'i', 'o', 'u'];
const visited = Array.from({ length: word_arr.length }, () => false);
let ans = Array.from({ length: (+n) }, () => '');
const dfs = (cnt, v, c, p) => {
    if (cnt === (+n)) {
        if (v > 0 && c > 1) console.log(ans.join(""));
        return;
    }
    for (let i = 0; i < word_arr.length; i++) {
        let check = false;
        if (visited[i]) continue;
        if (p > word_arr[i]) continue;
        visited[i] = true;
        if (vowel.indexOf(word_arr[i]) === -1) check = true;
        ans[cnt] = word_arr[i];
        dfs(cnt + 1, check ? v : v + 1, check ? c + 1 : c, word_arr[i]);
        visited[i] = false;
    }
}
dfs(0, 0, 0, 'A');
