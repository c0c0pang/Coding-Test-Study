/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const s_str = s.split("").sort().join("");
    const t_str = t.split("").sort().join("");
    console.log(s_str,t_str)
    if(s_str===t_str) return true;
    return false
};