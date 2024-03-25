# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        
        temp_node = ListNode()
        temp_node.next = head
        curr = temp_node

        for i in range(left - 1):
            curr = curr.next
        
        unchanged = curr
        pre_curr = None
        curr = curr.next

        for i in range(right - left + 1):
            curr.next, pre_curr, curr = pre_curr, curr, curr.next

        # change first reversed element next to element after last changed
        unchanged.next.next = curr
        # change left - 1 elements next to last changed
        unchanged.next = pre_curr

        return temp_node.next
        