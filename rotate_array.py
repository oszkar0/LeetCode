# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate_0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        shifted_number = nums[-1]
        reversed_indexes = reversed(range(len(nums)))
        for i in range(k):
            shifted_number = nums[-1]
            for j in reversed_indexes:
                nums[j] = nums[j - 1]
            nums[0] = shifted_number

    def rotate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)
        nums[:] = nums[-steps:] + nums[:-steps]

    def test(self):
        nums = [1,2,3,4,5,6,7]
        expected_arr = [5,6,7,1,2,3,4]
        self.rotate_1(nums, 3)

        if nums == expected_arr:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
   
    