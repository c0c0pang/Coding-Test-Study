/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let start = 0;
    let end = nums.length;
    let answer = -1;
    while(start<=end){
        let mid = parseInt((start+end)/2);
        console.log(start,end)
        if(nums[mid]===target){
            answer = mid;
            break;
        }
        if(nums[mid]>target){
            end = mid-1;
        }
        else{
            start = mid+1;
        }
    }
    return answer;
};

//이진 탐색 문제
//start,mid,end 세개의 변수를 이용해서 푼다.
//mid와 target을 비교하여 mid의 값이 더 크면 start의 값을 mid로 아니라면 end의 값을 mid로 변경
//종료 시점은 start가 end보다 커지는 경우에 종료한다.