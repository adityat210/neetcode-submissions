class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #need to return smallest i and end j index for the two numbers that add up to target
        #can create a dictionary to search in constant time if can create a specific value to look for
        #can look for target num, remaineder after target-nums[i] where i is the current index
        findNum = {}

        for i in range(len(nums)):
            target_num = target - nums[i]
            #check if the target num is in the dictionary
            if target_num in findNum:
                #if found, return [the index of the target num, i]
                return [findNum.get(target_num),i]

            #if not, add the current number to the dictionary with the index as the value
            findNum[nums[i]] = i
        
        
        
        
        
        
        
        #findNum = {}
        #for i in range(len(nums)):
        #    new_target = target - nums[i]
        #    if new_target in findNum:
        #        print(new_target)
        #        return [findNum[new_target],i]
        #    findNum[nums[i]] = i


