# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

class Solution(object):
    def isPalindrome_0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(filter(lambda x : x in "qwertyuiopasdfghjklzxcvbnm1234567890", list(s.lower())))
        i = 0
        j = len(s) - 1

        if len(s) == 0:
            return True

        while i <= len(s) // 2:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
    def isPalindrome_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(filter(lambda x : x in "qwertyuiopasdfghjklzxcvbnm1234567890", list(s.lower())))
        return s == s[::-1]
    
    def test(self):
        s = "A man, a plan, a canal: Panama"
        r = self.isPalindrome_0(s)

        if r:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()