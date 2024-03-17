class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_range = 0
        for num in nums:
            if max_range < 0:
                return False
            elif num > max_range:
                max_range = num
            max_range = max_range - 1
        return True

    def test(self):
        nums = [2,3,1,1,4]
        expected_return = True
        actual_return = self.canJump(nums)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   