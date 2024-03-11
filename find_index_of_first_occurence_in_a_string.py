# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr_0(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(1, len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                else:
                    return i

        return -1

    def strStr_1(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
    def test(self):
        haystack = "sadbutsad"
        needle = "sad"
        expected_index = 0
        actual_index = self.strStr_0(haystack, needle)
        

        if actual_index == expected_index:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()