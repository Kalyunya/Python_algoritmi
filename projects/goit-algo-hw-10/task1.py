import time

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    dp = [float("inf")] * (amount + 1)
    last_coin = [0] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}

    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
    amount = 113

    print("Жадібний алгоритм:")
    print(find_coins_greedy(amount))

    print("\nДинамічне програмування:")
    print(find_min_coins(amount))

    test_amount = 10000

    start = time.time()
    find_coins_greedy(test_amount)
    greedy_time = time.time() - start

    start = time.time()
    find_min_coins(test_amount)
    dp_time = time.time() - start

    print(f"\nGreedy time: {greedy_time:.6f} sec")
    print(f"DP time: {dp_time:.6f} sec")