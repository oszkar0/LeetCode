# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        count_map = {}
        
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] > n:
                return num
        
        return -1
    
    def test(self):
        nums = [2,2,1,1,1,2,2]
        r = 2
        k = self.majorityElement(nums)

        if r == k:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
