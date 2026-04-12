class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = minimum number of coins needed to make amount 'a'
        # Initialize with a value greater than any possible answer (acts like infinity)
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Build solutions for all amounts from 1 to target
        for a in range(1, amount + 1):

            # Try using each coin as the LAST coin for amount 'a'
            for c in coins:

                # Only valid if coin can contribute to current amount
                if a - c >= 0:

                    # If we take coin 'c', we reduce the problem to (a - c)
                    # So total coins = 1 (current coin) + best solution for (a - c)
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] is still "infinity", it means it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1