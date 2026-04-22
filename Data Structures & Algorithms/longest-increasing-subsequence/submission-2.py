class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Let T(i) = length of the longest strictly increasing subsequence in nums from 1...i
        #Recursive: T(i) = 1 + max_{T(j) s.t. a_j < a_i and j < i}
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])   
        return max(dp)
