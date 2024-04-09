class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            global_max = max(global_max, curr_max)

            curr_min = min(curr_min + num, num)
            global_min = min(global_min, curr_min)

            total += num

        return max(global_max, total -  global_min) if global_max > 0 else global_max