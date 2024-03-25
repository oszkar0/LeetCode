# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast, slow = head, head

        # give fast n nodes head start
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
        


        