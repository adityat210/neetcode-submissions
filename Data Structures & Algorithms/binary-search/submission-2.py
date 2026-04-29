class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #need to iteratively go through the array and see if you can narrow down the possible window for the target

        #starting at the end points of the array
        left, right = 0, len(nums) - 1
        #need to ensure the left is always <= than the right
        while left <= right:
            #need to update the middle index every time
            middle = left + ((right-left)//2)

            #if the target value is greater than the middle value we want the right of the window
            if target > nums[middle]:
                left = middle + 1
            #if the target value is less than the middle value we want the left half of the window
            elif target < nums[middle]:
                right = middle - 1
            #the target matches the middle value exactly
            else:
                return middle
        return -1
        



