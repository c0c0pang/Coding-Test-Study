/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let answer;
    const LEN = nums.length;
    for(let i=0;i<LEN;i++){
        let array = []
        let check = false
        let num = 0
        for(let j=i+1;j<LEN;j++){
            if(nums[i]+nums[j] === target){
                check = true
                num = j
                break
            }
        }
        if(check){
            answer = [i,num]
            break
        }
    }
    return answer
};