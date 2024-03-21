# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        output = []
        level_sum = 0

        while len(queue):
            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)
                level_sum += node.val 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            output.append(float (level_sum) / level_size)
        
        return output

        