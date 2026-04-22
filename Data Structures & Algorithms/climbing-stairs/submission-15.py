class Solution:
    def climbStairs(self, n: int) -> int:
    #let T(i) = the number of distinct ways to get to step i
    #Recursive = T(i) = T(i-1) + T(i-2)
        dp = {}

        def backtrack(i):
            if i == n:
                #distinct path is found
                return 1
            elif i > n:
                #out of bounds index return 0
                return 0
            if i in dp:
                return dp[i]
            dp[i] = backtrack(i+1) + backtrack(i+2)
            return dp[i]

        return backtrack(0)
                
            

        