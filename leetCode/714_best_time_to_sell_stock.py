class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = [-1e9]+[0]*len(prices)
        cash = [0]*(len(prices)+1)
        prices = [0]+prices
        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], cash[i-1]-prices[i])
            cash[i] = max(cash[i-1], hold[i-1]+prices[i]-fee)
        return cash[-1]