class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = 0; sell = 1
        max_profit = 0
        
        for sell, price in enumerate(prices):
            profit = price - prices[buy]
            if profit < 0:
                buy = sell
            else:
                max_profit = max(max_profit, profit)

        return max_profit

            