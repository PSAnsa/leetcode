/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    const set1 = new Set(nums1.map(Number));
    const set2 = new Set(nums2.map(Number));
    console.log(set1)
    const distinctsum1 = [];
    const distinctsum2 = [];
    for (const num of set1){
        if(!set2.has(num)){
            distinctsum1.push(num)
        }

    }
    for (const num of set2){
        if(!set1.has(num)){
            distinctsum2.push(num)
        }
    }

    return [distinctsum1, distinctsum2]
    
};