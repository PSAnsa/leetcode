class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums[1:])
        if nums[0]  == right + nums[0]:
            return 0
        for ptr in range(1,len(nums)):
            left += nums[ptr - 1]
            right -= nums[ptr]
            if left == right:
                return ptr
        return -1


        