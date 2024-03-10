class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_num = nums[0]
        num_count = 0
        i = 0
        while i < len(nums):
            if nums[i] == current_num:
                num_count += 1
                if num_count > 2:
                    nums.pop(i)
                    continue
            else:
                num_count = 1
                current_num = nums[i]
            i += 1
    
    def test(self):
        nums = [0,0,1,1,1,1,2,3,3]
        expected_arr = [0,0,1,1,2,3,3]

        self.removeDuplicates(nums)

        if nums == expected_arr:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
