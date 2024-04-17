class Solution(object):
    def maximalSquare0(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, down, diag)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2
                    

    def maximalSquare1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        dp = [[0] * (COLS + 1) for i in range(ROWS + 1)]
        max_size = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "1":
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                    max_size = max(max_size, dp[r + 1][c + 1])
        
        return max_size ** 2
        
        