class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            # left neighbor greater
            if m > 0 and nums[m] < nums[m - 1]:
                right = m - 1
            # right neigbhor greater 
            elif m < len(nums) -1 and nums[m] < nums[m + 1]:
                left = m + 1
            else:
                return m

