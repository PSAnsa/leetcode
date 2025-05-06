class Solution(object):
    def buildArray(self, nums):
        arr = []
        for i in range(len(nums)):
            # val = nums[i]
            arr.append(nums[nums[i]])
        return arr