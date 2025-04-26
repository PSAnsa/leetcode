class Solution(object):
    def longestOnes(self, nums, k):
        largest = 0
        left = 0
        zerocount = 0 
        for right in range(len(nums)):
            if(nums[right] == 0):
                zerocount += 1
            if(zerocount > k):
                if(nums[left] == 0):
                    zerocount -= 1
                left += 1
            #largest sliding window
            #right - left + 1 is sliding window size
            largest = max(largest, right-left+1)
        return largest