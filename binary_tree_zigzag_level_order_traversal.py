# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if not root:
            return result

        q = collections.deque([root])


        while q:
            q_length = len(q) 
            level = []

            for i in range(q_length):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if len(result) % 2:
                level.reverse()
            
            if level:
                result.append(level)

        return result