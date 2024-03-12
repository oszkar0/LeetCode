# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine.remove(ransomNote[i])
            else:
                return False
        
        return True

    def test(self):
        ransom_note = "aa"
        magazine = "aab"
        expected_return = True
        actual_return = self.canConstruct(ransom_note, magazine)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()