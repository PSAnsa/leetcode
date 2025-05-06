class Solution(object):
    def buildArray(self, nums):
        arr = [0] * len(nums)
        for i in range(len(nums)):
            val = nums[i]
            arr[i] = nums[val]
        return arr