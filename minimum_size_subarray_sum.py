# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
import sys

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        min_size = sys.maxsize
        i = 0
        j = 0
        n = len(nums)

        while i < n and j < n:
            if sum < target:
                j += 1
                if j == n:
                    break
                sum += nums[j]
            else: 
                if j - i + 1 < min_size:
                    min_size = j - i + 1
                sum -= nums[i]
                i += 1

        return min_size 

    def test(self):
        nums = [2,3,1,2,4,3]
        target = 7
        expected_return = 2

        actual_return = self.minSubArrayLen(target, nums)

        if expected_return == actual_return:
            print('Test passed!')
        else:
            print('Test failed:')
 
if __name__ == '__main__':
    solution = Solution()
    solution.test()

        