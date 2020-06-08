class Solution:
    # coins: List[int]
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for coin_range in range(coin, amount + 1):
                dp[coin_range] += dp[coin_range - coin]
        return dp[amount]

solution = Solution()
amount = 5
coins = [1,2,5]
print(solution.change(amount, coins))