class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        board.reverse()

        def intToPos(square):
            r = (square - 1) // len(board)
            c = (square - 1) % len(board)

            if r % 2:
                c = len(board) - 1 - c

            return [r, c]                

        q = collections.deque() # [square, moves]
        q.append([1, 0])
        visited = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                next_square = square + i
                r, c = intToPos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square >= len(board) * len(board[0]):
                    return moves + 1

                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square, moves + 1])
        
        return -1

                    

