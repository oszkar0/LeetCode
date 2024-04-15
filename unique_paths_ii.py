class Solution(object):
    def uniquePathsWithObstacles0(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        dp = {(M - 1, N - 1): 1}

        def dfs(r, c):
            if r == M or c == N or grid[r][c]:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]
        
        return dfs(0, 0)
    
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
                ## else dp[c] = dp[c]

        return dp[0]