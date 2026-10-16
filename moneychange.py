def coinChange(coins, amount):
    INF = float('inf')
    dp = [INF] * (amount + 1)   # the table
    dp[0] = 0                   # 0 cents needs 0 coins

    for a in range(1, amount + 1):      # outer loop: money times
        for coin in coins:              # inner loop: d times
            if coin <= a:               # skip coins that are too big
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != INF else -1
print(coinChange([1, 5, 6], 9))   # 4
print(coinChange([5], 3))         # -1  (impossible)
print(coinChange([1, 8, 20], 24)) # 3   (8+8+8, the greedy-fails case)


# ---------------------------------------------------------
# MONEY CHANGE (Coin Change)
# ---------------------------------------------------------
# PROBLEM
# Given coin denominations and an amount, find the minimum
# number of coins that make the amount exactly.
# If it is impossible, return -1.
# Example: coins [1, 5, 6], amount 9 -> 4 (6+1+1+1)
# Greedy can fail: coins [1, 8, 20], amount 24
#   greedy = 20+1+1+1+1 (5 coins), best = 8+8+8 (3 coins)
#
# HOW DID WE DO IT (Dynamic Programming)
# 1. dp[a] = minimum coins needed to make a cents.
# 2. dp[0] = 0, because 0 cents needs 0 coins.
# 3. Fill the table from left to right, 1 up to amount.
# 4. For each amount, try every coin that fits:
#    dp[a] = min(dp[a], dp[a - coin] + 1)
# 5. Each small answer is solved once and stored,
#    so we never repeat work.
# 6. Return dp[amount], or -1 if it was never solved.
#
# TIME COMPLEXITY
# Time:  O(amount * d), d = number of coin types.
#   Outer loop runs amount times, inner loop runs d times.
#   Skipping a coin that is too big still counts as a step.
#   Example: amount 9, 3 coins -> 9 * 3 = 27 steps.
# Space: O(amount), for the dp table.
# ---------------------------------------------------------