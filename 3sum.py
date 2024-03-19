class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        unique_triplets = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == target:
                    unique_triplets.add((nums[i], nums[j], nums[k]))
                    j = j + 1
                    k = k - 1
                elif sum < target:
                    j = j + 1
                else:
                    k = k - 1
        
        return list(unique_triplets)

    def test(self):
        nums = [-1,0,1,2,-1,-4]
        expected_return = [(-1, 0, 1), (-1, -1, 2)]
        actual_return = self.threeSum(nums)

        if expected_return == actual_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
