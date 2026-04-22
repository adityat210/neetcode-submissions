class Solution:
    def climbStairs(self, n: int) -> int:
    #let T(i) = the number of distinct ways to get to step i
    #Recursive = T(i) = T(i-1) + T(i-2)
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
                
            

        