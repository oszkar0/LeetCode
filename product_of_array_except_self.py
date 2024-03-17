class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre_number = [1] * len(nums)
        post_number = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_number[i] = pre_number[i - 1] * nums[i - 1]

        
        for i in range(len(nums) - 2, -1, -1):
            post_number[i] = post_number[i + 1] * nums[i + 1]
        
        return [pre_number[i] * post_number[i] for i in range(len(nums))]
    
    def test(self):
        nums = [1,2,3,4]
        expected_return = [24,12,8,6]
        actual_return = self.productExceptSelf(nums)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   