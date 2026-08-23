class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        max_profit = 0
        lp = prices[0]
        for i in range(len(prices)):
            if prices[i]<lp:
                lp = prices[i]
                print(i,lp)
            else:
                profit = prices[i]-lp
                print(i,max_profit)
                max_profit = max(profit,max_profit)
        
        return max_profit