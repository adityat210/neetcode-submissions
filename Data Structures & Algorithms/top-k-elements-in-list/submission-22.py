class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #keep track of count
        count = {}
        #keep frequency array after iterating through list once
        frequency = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = 1 + count.get(nums[i])
            else:
                count[nums[i]] = 1
        for n, c in count.items():
            frequency[c].append(n)

        #need to find result array
        result = []
        #will backtrack from frequency
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result






















        ##going to keep track of occurences
        ##keep count of every digit
        #count = {}
        #freq = [[] for i in range(len(nums) + 1)]

        #for i in range(len(nums)):
         #   count[nums[i]] = 1 + count.get(nums[i], 0)
        ##frequency of every item ordered
        #for n,c in count.items():
         #   freq[c].append(n)
        #go backwards adding from frequency till result length is met for k
        #result = []
        #for i in range(len(freq)-1, 0, -1):
         #   for n in freq[i]:
          #      result.append(n)
           #     if len(result) == k:
            #        return result