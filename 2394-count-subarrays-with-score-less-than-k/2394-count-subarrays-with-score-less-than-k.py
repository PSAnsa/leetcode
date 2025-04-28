class Solution(object):
    def countSubarrays(self, nums, k):
        output = 0
        currentsums = 0
        left = 0
        for right in range(len(nums)):
            currentsums += nums[right]
            while left <= right and currentsums * (right-left+1) >= k:
                currentsums -= nums[left]
                left += 1
            output += (right-left+1)
        return output