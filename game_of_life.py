class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # all new 0 -> 2
        # all new 1 -> 3
        rows, cols = len(board), len(board[0])
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

        for row in range(rows):
            for col in range(cols):
                live_neighbor = 0
                # count live neighbors
                for row_dir, col_dir in dirs:
                    n_row, n_col = row + row_dir, col + col_dir
                    if 0 <= n_row < rows and 0 <= n_col < cols and (board[n_row][n_col] == 1 or board[n_row][n_col] == 2):
                        live_neighbor += 1

                # apply rules
                if board[row][col] == 1 and (live_neighbor < 2 or live_neighbor > 3):
                     board[row][col] = 2

                if board[row][col] == 0 and live_neighbor == 3:
                     board[row][col] = 3

        # replace 2 and 3 
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2: board[row][col] = 0
                elif board[row][col] == 3: board[row][col] = 1


