class Solution(object):
    def maxProfit_0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        
        return max_profit
    
    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else: 
                left = right
            right += 1

        return max_profit
    
    def test(self):
        prices = [7,1,5,3,6,4]
        expected_profit = 5

        actual_profit = self.maxProfit_1(prices)

        if actual_profit == expected_profit:
            print('Test passed!')
        else:
            print('Test failed!')

if __name__ == '__main__':
    solution = Solution()
    solution.test()
