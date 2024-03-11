class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True

        s_ptr = 0
        for i in range(len(t)):
            if s[s_ptr] == t[i]:
                s_ptr += 1
            
            if s_ptr >= len(s):
                return True

        return False
    
    def test(self):
        s = "abc"
        t = "ahbgdc"
        r = self.isSubsequence(s, t)

        if r:
            print('Test passed!')
        else:
            print('Test failed:')
 
if __name__ == '__main__':
    solution = Solution()
    solution.test()
