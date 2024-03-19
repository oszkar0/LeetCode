class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x[0])

        i, j = 0, len(nums) - 1
        nums.sort()

        while i < j:
            if nums[i][0] + nums[j][0] == target:
                return [nums[i][1], nums[j][1]]
            elif nums[i][0] + nums[j][0] < target:
                i = i + 1
            else:
                j = j - 1
            
        
    def test(self):
        nums = [3,2,4]
        target = 6
        expected_return = [1, 2]
        actual_return = self.twoSum(nums, target)

        if expected_return == actual_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()