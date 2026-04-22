class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Let T(i) = the minimum cost to reach top of the staircase from step i
        #Recursive: T(i) = min(T(i-1) + cost[i-1], T(i-2) + cost[i-2])

        dp = {}

        def backtrack(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(backtrack(i+1), backtrack(i+2))
            return dp[i]
        
        return min(backtrack(0), backtrack(1))
        