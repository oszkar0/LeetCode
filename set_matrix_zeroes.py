class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 

        rows, cols = len(matrix), len(matrix[0])
        zero_first_row = not all(matrix[0])
        zero_first_col = False

        # find zeros in first column
        for row in matrix:
            if row[0] == 0:
                zero_first_col = True
                break
        
        # find zeros inside matrix (not first col and not first row)
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0

        # put zeros inside matrix (not first col and not first row)        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # put zeros in first row and col
        if zero_first_row:
            matrix[0] = [0] * cols
        
        if zero_first_col:
            for row in matrix:
                row[0] = 0
                
        