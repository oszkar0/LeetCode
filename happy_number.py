class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        current_number = n
        sum = 0
        sums = set()

        while True:
            for i in str(current_number):
                sum += int(i) ** 2

            if sum == 1:
                return True
            
            if sum in sums:
                return False
            
            sums.add(sum)
            current_number = sum
            sum = 0


    def test(self):
        n = 19
        expected_return = True
        actual_return = self.isHappy(n)

        if actual_return == expected_return:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()   