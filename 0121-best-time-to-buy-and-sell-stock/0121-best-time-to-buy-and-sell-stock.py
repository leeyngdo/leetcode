class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = 0; sell = 1
        max_profit = 0
        
        while sell <= len(prices) - 1:
            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell
            else:
                max_profit = max(max_profit, profit)
            
            sell += 1

        return max_profit

            