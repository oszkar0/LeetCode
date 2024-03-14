# Given an integer, convert it to a roman numeral.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_number = ""
        roman_digits = [
            [1000, "M"], [900, "CM"], [500, "D"], 
            [400, "CD"], [100, "C"], [90, "XC"], 
            [50, "L"], [40, "XL"], [10, "X"],
            [9, "IX"], [5, "V"], [4, "IV"],
            [1, "I"]]
        for i in range(len(roman_digits)):
            while num >= roman_digits[i][0]:
                roman_number += roman_digits[i][1]
                num -= roman_digits[i][0]

        return roman_number
    
    def test(self):
        number_to_convert = 1994
        expected_return = "MCMXCIV"
        actual_return = self.intToRoman(number_to_convert)

        if expected_return == actual_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
