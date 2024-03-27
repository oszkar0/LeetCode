# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []

        while root or stack:
            # go to the leftmost element
            while root:
                stack.append(root)
                root = root.left
            
            # pop last element inorder (visit)
            root = stack.pop()
            k -= 1

            # if we visited k elements we return else go to right subtree 
            if k == 0:
                return root.val
            root = root.right



