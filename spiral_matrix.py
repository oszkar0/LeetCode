class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        output = []

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top = top + 1

            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right = right - 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom = bottom - 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left = left + 1
            
        return output


    def test(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected_return = [1,2,3,6,9,8,7,4,5]
        actual_return = self.spiralOrder(matrix)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
