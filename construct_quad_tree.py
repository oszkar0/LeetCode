import itertools


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def dfs(n, r, c):
            all_same = True

            for i, j in itertools.product(range(0, n), range(0, n)):
                if grid[r][c] != grid[r + i][c + j]:
                    all_same = False
                    break

            if all_same:
                return Node(grid[r][c], isLeaf = True)

            n = n // 2
            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)
            return Node(None, False, top_left, top_right, bottom_left, bottom_right)
    
        return dfs(len(grid), 0, 0)