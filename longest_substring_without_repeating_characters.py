# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        l = 0
        seen_letters = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen_letters:
                seen_letters.remove(s[l])
                l += 1
            seen_letters.add(s[r])
            max_length = max(max_length, len(seen_letters))
        
        return max_length
    
    def test(self):
        s = "abcabcbb"
        expected_return = 3
        actual_return = self.lengthOfLongestSubstring(s)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
