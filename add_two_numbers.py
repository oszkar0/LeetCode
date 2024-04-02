# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = dummy = ListNode()
        
        residual = 0
        while l1 and l2:
            digit = l1.val + l2.val + residual
            residual = 0
            if digit > 9:
                residual = 1
                digit = digit % 10
            
            temp.next = ListNode(digit)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                digit = l1.val + residual
                residual = 0
                if digit > 9:
                    residual = 1
                    digit = digit % 10
                temp.next = ListNode(digit)
                temp = temp.next
                l1 = l1.next
                    
        if l2:
            while l2:
                digit = l2.val + residual
                residual = 0
                if digit > 9:
                    residual = 1
                    digit = digit % 10
                temp.next = ListNode(digit)
                temp = temp.next
                l2 = l2.next
        
        if residual == 1:
             temp.next = ListNode(1)
        
        return dummy.next