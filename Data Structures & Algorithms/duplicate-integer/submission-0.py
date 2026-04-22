class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Let T(i) be the maximum number of times a given integer appears in the array
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True

        return False

        