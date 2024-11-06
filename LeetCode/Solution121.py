from typing import List


class Solution121:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > profit:
                profit = price - minPrice
        return profit
