class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        for num in nums:
            if len(output) > 0 and output[-1][1] == num - 1:
                output[-1][1] = num
            else:
                output.append([num, num])

        return [f'{x}->{y}' if x != y else f'{x}' for x, y in output]

    def test(self):
        nums = [0,1,2,4,5,7]
        expected_return = ["0->2","4->5","7"]
        actual_return = self.summaryRanges(nums)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()       