class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def backtrack(index):
            if index == n:
                return 1
            if index > n:
                return 0
            if index in dp:
                return dp[index]
            dp[index] = backtrack(index+1) + backtrack(index+2)
            return dp[index]
        
        return backtrack(0)