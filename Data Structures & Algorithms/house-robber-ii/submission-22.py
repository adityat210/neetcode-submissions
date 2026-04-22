class Solution:
    def rob(self, nums: List[int]) -> int:
        #Let T(i) = maximum amount of money possible without alerting Police
        #Recursion: T(i) = max(nums[i] + T(i-2), T(i-1): s.t. !(i == 0 ^ i+2 = len(nums)); 0 <= i <= len(nums))
        if len(nums) == 1:
            return nums[0]
        
        def solve(arr):
            dp = {}

            def backtrace(index):
                if index >= len(arr):
                    return 0
                if index in dp:
                    return dp[index]
                dp[index] = max(backtrace(index+1), backtrace(index+2)+arr[index])
                return dp[index]
            
            return backtrace(0)
        
        return max(solve(nums[1:]), solve(nums[:-1]))
                
