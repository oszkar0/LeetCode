# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                top_left = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left

            left += 1
            right -= 1

    def test(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected_matrix = [[7,4,1],[8,5,2],[9,6,3]]
    
        self.rotate(matrix)

        if expected_matrix == matrix:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()