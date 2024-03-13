class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x: x[0])
        merged_intervals = [intervals[0]]
        for interval in intervals:
            if merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])

        return merged_intervals
    
    def test(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected_output = [[1,6],[8,10],[15,18]]
        output = self.merge(intervals)

        if output == expected_output:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
