class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd length
            l, r = i , i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = len(res)
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = len(res)
                l -= 1
                r += 1

        return res