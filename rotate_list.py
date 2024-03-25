# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        curr = head
        length = 1

        # connect tail and head
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        
        # disconnect in the new head/tail place
        new_head_pos = length - (k % length)

        while new_head_pos > 0:
            curr = curr.next
            new_head_pos -= 1

        new_head = curr.next
        curr.next = None

        return new_head

        