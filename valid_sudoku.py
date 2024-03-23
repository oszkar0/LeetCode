class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for x in range(9)]
        columns = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]

        for x in range(9):
            for y in range(9):
                cell = board[x][y]

                if cell == '.':
                    continue
                
                if cell in rows[x] or cell in columns[y] or cell in squares[x // 3][y // 3]:
                    return False
                
                rows[x].add(cell)
                columns[y].add(cell)
                squares[x // 3][y // 3].add(cell)
        
        return True