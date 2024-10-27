def maximum_profit(prices):
    max_profit = 0
    current_index = 0
    for i in range(1, len(prices)):
        current_profit = prices[i] - prices[current_index]
        max_profit = max(max_profit, current_profit)
        if current_profit < 0:
            current_index = i

    return max_profit


print(maximum_profit([1, 2, 3, 4, 5]))