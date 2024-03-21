# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = float('inf')
        self.min_diff = float('inf')

    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)

        self.min_diff = min(self.min_diff, abs(self.prev - root.val))
        self.prev = root.val

        if root.right:
            self.inOrder(root.right)


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inOrder(root)
        return self.min_diff
        