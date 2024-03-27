import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def mark_island(r, c):
            q = collections.deque()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            q.append((r, c))
            while q:
                r, c = q.popleft()        
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col)) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    mark_island(r, c)
                    islands += 1

        return islands