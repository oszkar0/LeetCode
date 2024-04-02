class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        b = n

        if x == 0:
            return 0
        elif n == 0:
            return 1
        elif b < 0:
            x = 1 / x
            n = -n

        a = 1
        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n // 2
            else:
                n -= 1
                a = a * x 

        return a
        