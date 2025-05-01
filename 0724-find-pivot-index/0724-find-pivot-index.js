/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let right = nums.slice(1).reduce((acc, val) => acc + val, 0)
    let left = 0
    if(right +  nums[0] == nums[0]) { return 0}
    for(let i = 1; i< nums.length; i++){
        right -= nums[i - 1]
        left += nums[i]
        if(left == right){ return i }
    }
    return -1
};