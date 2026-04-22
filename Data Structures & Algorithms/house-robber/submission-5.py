class Solution:
    def rob(self, nums: List[int]) -> int:
        #Let T(i) = maximum amount of money you can rob from string nums[1...i] without alerting the police.
        #Recursive: T(i) = max(T(i-1), T(i-2) + nums[i])
        dp = {}

        def backtrack(index):
            if index >= len(nums):
                return 0
            if index in dp:
                return dp[index]
            dp[index] = max(backtrack(index+1), backtrack(index+2)+nums[index])
            return dp[index]
        
        return backtrack(0)

        