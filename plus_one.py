class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1

        while digits[i] == 9:
            digits[i] = 0
            i = i - 1
        
        if i < 0:
            digits  = [1] + digits
        else:
            digits[i] = digits[i] + 1
    
        return digits


