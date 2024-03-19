class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        direction = 1 
        row = 0

        for char in s:
            rows[row] += char

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return ''.join(rows)
    
    def test(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected_return = "PAHNAPLSIIGYIR"
        actual_return = self.convert(s, numRows)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   