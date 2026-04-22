class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        findNum = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in findNum:
                print(new_target)
                return [findNum[new_target],i]
            findNum[nums[i]] = i


