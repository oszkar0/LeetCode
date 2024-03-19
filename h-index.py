class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        citations.sort(reverse=True)

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1

        return h 
    

    def test(self):
        citations = [3,0,6,1,5]
        expected_return = 3
        actual_return = self.hIndex(citations)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   