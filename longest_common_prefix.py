class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for i in range(1, len(strs)):
            while prefix != strs[i][:len(prefix)]:
                prefix = prefix[:-1]
                if prefix == "":
                    return prefix
        
        return prefix