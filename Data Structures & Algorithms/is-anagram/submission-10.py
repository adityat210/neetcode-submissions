class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        return countS == countT
            
        
        
        
        
        
        
        
        
        #return sorted(s) == sorted(t)







        #base case, if s and t are not in same length, cannot be anagrams
        #if len(s) != len(t):
         #   return False

        # if they are anagrams, they have to have the same count for the given letter
        #HashS, HashT = {}, {}
        #for i in range(len(s)):
        #    HashS[s[i]] = 1 + HashS.get(s[i],0)
        #    HashT[t[i]] = 1 + HashT.get(t[i],0)
        
        #return HashS == HashT
        
        #return sorted(s) == sorted(t)