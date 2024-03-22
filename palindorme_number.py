class Solution(object):
    def isPalindrome0(self, x):
        if x < 0:
            return False

        return str(x) == str(x)[::-1]
        
    def isPalindrome1(self, x):
        if x < 0:
            return False
        
        num = x
        backward_num = 0

        while x > 0:
            backward_num = backward_num * 10 + x % 10
            x = x // 10
        
        return backward_num == num
        