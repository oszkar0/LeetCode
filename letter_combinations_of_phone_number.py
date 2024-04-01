class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curr_string):
            if len(curr_string) == len(digits):
                result.append(curr_string)
                return

            for c in keyboard[digits[i]]:
                backtrack(i + 1, curr_string + c)

        if digits:
            backtrack(0, "")

        return result