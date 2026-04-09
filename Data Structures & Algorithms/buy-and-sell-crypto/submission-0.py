class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<1:
            return 0
        first_day=prices[0]
        profit=0
        for i in range(1,n):
            if prices[i]>first_day:
                profit=max(profit,prices[i]-first_day)
            else:
                first_day=prices[i]
        return profit