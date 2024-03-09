class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        
        return i
    
    def test(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        expected_arr = [0,1,3,0,4]
        expected_k = 5
        k = self.removeElement(nums, val)

        if nums == expected_arr and k == expected_k:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
