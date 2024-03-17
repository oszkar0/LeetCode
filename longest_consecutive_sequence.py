class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        max_length = 1
        length = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                length = length + 1
                max_length = max(max_length, length)
            else:
                length = 1

        return max_length

    def test(self):
        nums = [1,2,0,1]
        expected_return = 3
        actual_return = self.longestConsecutive(nums)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   