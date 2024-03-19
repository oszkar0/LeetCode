class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        output = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman_digits[s[i]] < roman_digits[s[i + 1]]:
                output = output - roman_digits[s[i]]
            else:
                output = output + roman_digits[s[i]]

        return output
    
    def test(self):
        s = "MCMXCIV"
        expected_return = 1994
        actual_return = self.romanToInt(s)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   