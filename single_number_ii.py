class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            bit_count = 0
            for n in nums:
                temp = n >> i
                temp = temp & 1
                bit_count += temp
            
            rem = bit_count % 3

            if i == 31 and rem:
                ans -= 1 << 31
            else:
                ans |= rem << i

        return ans
