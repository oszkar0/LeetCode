
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        visited = {None: None}
        curr = head

        while curr:
            if curr not in visited:
                visited[curr] = Node(curr.val)
            if curr.next not in visited:
                visited[curr.next] = Node(curr.next.val)
            if curr.random not in visited:
                visited[curr.random] = Node(curr.random.val)

            visited[curr].next = visited[curr.next]
            visited[curr].random = visited[curr.random]
            curr = curr.next
        
        return visited[head]