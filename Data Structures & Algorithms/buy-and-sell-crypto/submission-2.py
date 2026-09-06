class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # indexes

        buy = 0
        sell = 1

        while sell < len(prices):
            max_profit = max(max_profit, prices[sell]-prices[buy])
            
            if prices[sell] < prices[buy]:
                buy = sell

            sell += 1

        return max_profit

