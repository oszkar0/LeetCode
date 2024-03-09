class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            i += 1
        
        return len(nums)
    
    def test(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_arr = [0,1,2,3,4]
        expected_k = 5

        k = self.removeDuplicates(nums)

        if nums == expected_arr and k == expected_k:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
