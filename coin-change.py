def coin_change(coins, amount, counter):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    if counter[amount] != float("inf"):
        return counter[amount]

    minimum = float("inf")
    for coin in coins:
        subproblem = coin_change(coins, amount - coin, counter)
        if subproblem >= 0 and subproblem < minimum:
            counter[amount] = min(counter[amount], 1 + subproblem)
    return counter[amount]

coins = [2]
amount = 3
counter = [float("inf") for i in range(amount + 1)]

def coin_change(coins, amount):
    counter = [float("inf")] * (amount + 1)
    counter[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and counter[i - coin] != float("inf"):
                counter[i] = min(counter[i], 1 + counter[i - coin])

    print(counter)
    return counter[amount] if counter[amount] != float("inf") else -1

print(coin_change(coins, amount))