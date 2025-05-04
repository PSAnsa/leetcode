class Solution(object):
    def findDifference(self, nums1, nums2):
       nums1 = set(nums1)
       nums2 = set(nums2)
       distinct_set1 = list(nums1-nums2)
       distinct_set2 = list(nums2- nums1)
       return [distinct_set1, distinct_set2]