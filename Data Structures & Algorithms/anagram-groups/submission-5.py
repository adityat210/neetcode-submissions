class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort every single string alphabetical ascending
        #can add every unique string to set if not found already
        #if found, append to an array of same category
        #could index through and if matches, add only the index and not the word itself, would make it easier to return the same category
        findCategory = {}
        sorted_array = []
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in findCategory:
                findCategory[sorted_word] = findCategory.get(sorted_word) + [i]
            else:
                sorted_array = sorted_array + [sorted_word]
                findCategory[sorted_word] = [i]
        
        outter = []
        for i in range(len(sorted_array)):
            inner = []
            if sorted_array[i] in findCategory:
                for j in findCategory.get(sorted_array[i]):
                    inner += [strs[j]]
            if inner != []:
                outter += [inner]

        return outter


        
        




        