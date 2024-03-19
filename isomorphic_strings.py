class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        letter_dict = {}

        for i in range(len(s)):
            if s[i] in letter_dict:
                if letter_dict[s[i]] != t[i]:
                    return False
            else: 
                letter_dict[s[i]] = t[i]

        return True
    
    def test(self):
        s = 'badc'
        t = 'baba'
        expected_return = False
        actual_return = self.isIsomorphic(s, t)

        if expected_return == actual_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()