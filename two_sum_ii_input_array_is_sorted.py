class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        curr_sum = numbers[left] + numbers[right]
        while curr_sum != target:
            if curr_sum > target:
                right -= 1
            else:
                left += 1
            curr_sum = numbers[left] + numbers[right]
        return [left + 1, right + 1]
    
    def test(self):
        nums = [2,7,11,15]
        target = 9
        expected_arr = [1, 2]

        ret = self.twoSum(nums, target)

        if ret == expected_arr:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
