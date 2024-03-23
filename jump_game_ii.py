class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        w_left, w_right = 0, 0

        while w_right < len(nums) - 1:
            furthest = 0
            for i in range(w_left, w_right + 1):
                furthest = max(furthest, i + nums[i])
            w_left = w_right + 1
            w_right = furthest
            jumps += 1
        
        return jumps
