class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = 0
        overall_max = float("-inf")

        for num in nums:
            curr_max = max(curr_max + num, num)
            overall_max = max(overall_max, curr_max)
        return overall_max