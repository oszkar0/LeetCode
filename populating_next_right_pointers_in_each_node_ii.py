
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        q = collections.deque([root])

        while q:
            q_length = len(q)
            dummy = Node()

            for i in range(q_length):
                node = q.popleft()
                dummy.next = node
                dummy = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root