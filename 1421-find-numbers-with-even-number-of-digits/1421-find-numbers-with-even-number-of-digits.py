class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in range(len(nums)):
            semicount = 0
            for digit in str(nums[i]):
                semicount += 1
            if semicount % 2 == 0:
                count += 1
        return count
        