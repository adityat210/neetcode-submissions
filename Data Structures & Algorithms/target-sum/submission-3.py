class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Let T(i, j) = number of different ways to assign plus or minus to the first i elements of nums so their sum is j
        #Recursion: T(i, j) = 1 + T(i-1,j-nums[i]) + T(i-1,j+nums[i])
        dp = {}
        def backtrack(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                else: return 0
            if (index, total) in dp:
                return dp[(index,total)]

            dp[(index, total)] = backtrack(index+1, total-nums[index])+ backtrack(index+1, total+nums[index])
            return (dp[(index,total)])

        return backtrack(0, 0)
