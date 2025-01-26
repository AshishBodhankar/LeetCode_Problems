def maxProfit(prices: list) -> int:
    l = len(prices)
    max_profit = float('-inf')
    for i in range(len(prices)-1):
        for j in range(i,len(prices)):
            profit = prices[j] - prices[i]

            if profit > 0:
                max_profit = max(max_profit,profit)
    return max_profit if max_profit > float('-inf') else 0
    # TIME: O(N^2)
    # SPACE: O(1)


def maxProfit2(prices: list) -> int:

    if len(prices) == 2 and prices[1] <= prices[0]: return 0

    l = len(prices)
    max_profit = 0
    min_price = float('inf')

    for i in range(1,l):
        min_price = min(min_price,prices[i-1])
        max_profit = max(max_profit,prices[i]-min_price)
    return max_profit

def maxProfit3(prices: list) -> int:

    max_profit = 0
    min_price = float('inf')

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price-min_price

        if profit > max_profit:
            max_profit = profit
    return max_profit