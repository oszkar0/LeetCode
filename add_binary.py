class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0: sum += int(a[i])
            if j >= 0: sum += int(b[j])
            i -= 1
            j -= 1

            carry = 1 if sum > 1 else 0
            res += str(sum % 2)

        if carry != 0: res += str(carry)
        return res[::-1]