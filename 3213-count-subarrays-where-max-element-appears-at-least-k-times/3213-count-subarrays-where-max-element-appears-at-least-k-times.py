class Solution(object):
    def countSubarrays(self, nums, k):
        maxs = 0
        maxcount = 0
        count = 0
        left = 0
        
        maxs = max(nums)
        for right in range(len(nums)):
            if nums[right] == maxs:
                count += 1
            while count == k:
                maxcount += len(nums) - right
                if nums[left] == maxs:
                    count -= 1
                left +=1
            # maxcount += (right -left +1)
        return maxcount


        