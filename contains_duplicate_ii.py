class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_set = {}

        for i in range(len(nums)):
            if nums[i] in index_set and abs(i - index_set[nums[i]]) <= k:
                return True
            index_set[nums[i]] = i

        return False
        
    def test(self):
        nums = [1,2,3,1,2,3]
        k = 2
        expected_return = False
        actual_return = self.containsNearbyDuplicate(nums, k)

        if expected_return == actual_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
    