class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reversed_num = 0

        for i in range(32):
            reversed_num = (reversed_num << 1) | (n & 1)
            n >>= 1

        return reversed_num