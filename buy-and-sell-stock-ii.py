def getMaxProfit(prices) -> int:
    profit = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit

print(getMaxProfit([1,2,3,1,5]))  # 6
print(getMaxProfit([3,2,1]))  # 0