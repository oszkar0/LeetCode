class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        i = 0

        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        
        return left << i