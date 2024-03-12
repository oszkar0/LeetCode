# Given a pattern and a string s, find if s follows the same pattern.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        symbol_dict = dict()
        s = s.split(' ')
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if not pattern[i] in symbol_dict.keys():
                symbol_dict[pattern[i]] = s[i]
                word = s[i]
            else:
                word = symbol_dict[pattern[i]]

            if len(set(symbol_dict.values())) != len(symbol_dict.values()):
                return False

            if word != s[i]:
                return False
        
        return True
    
    def test(self):
        pattern = "abba"
        s = "dog cat cat fish"
        actual_return = self.wordPattern(pattern, s)

        if not actual_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
