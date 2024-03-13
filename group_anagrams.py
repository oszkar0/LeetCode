# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()

        for word in strs:
            letters = "".join(sorted(word))

            if letters not in anagrams.keys():
                anagrams[letters] = []
            
            anagrams[letters].append(word)

        return anagrams.values()
    
    def test(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected_anagrams = [["eat","tea","ate"], ["tan","nat"],["bat"],]

        returned_anagrams = list(self.groupAnagrams(strs))

        if returned_anagrams == expected_anagrams:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()