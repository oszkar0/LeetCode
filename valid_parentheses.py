class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != brackets[stack.pop()]:
                return False
        
        return len(stack) == 0
    
    def test(self):
        s = "()[]{}"
        expected_return = True
        actual_return = self.isValid(s)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')

if __name__ == '__main__':
    solution = Solution()
    solution.test()