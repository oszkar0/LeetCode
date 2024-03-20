# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle0(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare = tortoise = head
        while hare and hare.next:
            tortoise, hare = tortoise.next, hare.next.next

            if hare == tortoise:
                return True

        return False
    
    def hasCycle1(self, head):
        seen = set()
        current = head

        while current:
            if current in seen:
                return True
            
            seen.add(current)
            current = current.next
            
        return False


            