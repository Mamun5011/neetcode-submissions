class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize default profit and buying_price

        max_Profit = 0
        buying_price = prices[0]

        # iterate over the array
        for i in range(len(prices)):
        # check the profit and update the maxprofit
            if prices[i] > buying_price:
                max_Profit = max(max_Profit, prices[i] - buying_price)
        # update buying price if applicable   
            if prices[i] < buying_price:
                buying_price = prices[i]     
        return max_Profit       
           


        
        