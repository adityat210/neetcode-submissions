class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Let T(i) = minimum cost to reach top from step i
        #recursive: T(i) = min(T(i-1)+cost[i-1], T(i-2)+cost[i-2])
        
        dp = {}
        def backtrack(index):
            if index >= len(cost):
                return 0
            if index in dp:
                return dp[index]
            dp[index] = min(backtrack(index+1), backtrack(index+2)) + cost[index]
            return dp[index]

        
        return min(backtrack(0),backtrack(1))

        