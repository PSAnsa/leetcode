import math
class Solution(object):
    def countSubarrays(self, nums):
        subarr = 0
        for i in range(len(nums)):
            sums = 0
            vals = 0
            if i < len(nums) and i+2 < len(nums):
                sums = nums[i] + nums[i+2]
                vals = float(nums[i+1]/2.0)
                if(sums == vals):
                    subarr += 1
        return subarr