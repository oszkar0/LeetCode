# Given a string s consisting of words and spaces, return the length of the last word in the string.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        start_counting = False
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ' and not start_counting:
                length = 1
                start_counting = True
            elif s[i] != ' ' and start_counting:
                length = length + 1
            elif s[i] == ' ' and start_counting:
                return length
            
            i = i - 1
        
        return length
    
    def test(self):
        s = "   fly me   to   the moon  "
        expected_return = 4
        actual_return = self.lengthOfLastWord(s)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()