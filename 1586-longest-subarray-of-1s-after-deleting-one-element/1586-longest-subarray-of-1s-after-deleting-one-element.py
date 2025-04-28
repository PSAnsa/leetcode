class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        largestSub = 0
        zerocount = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            if zerocount > 1:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
            largestSub = max(largestSub, right-left)
        return largestSub