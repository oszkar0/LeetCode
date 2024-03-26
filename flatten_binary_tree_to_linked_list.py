# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None

            left_tail = dfs(root.left)
            right_tail = dfs(root.right)

            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            last = right_tail or left_tail or root
            return last
        dfs(root)
        