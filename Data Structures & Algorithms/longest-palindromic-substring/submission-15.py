class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Let T(i, j) = the longest substring of s[i...j] that is a palindrome
        #Recursive:  T(i,j) = 
            #1 if i = j
            #1 if s[i] = s[j] and T(i+1, j-1) = 1
            #1 if j-i = 1

        #T(i,j)=whether substring s[i..j] is a palindrome
        #T(i,j)=1 if s[i]=s[j] and (j−i≤2 or T(i+1,j−1)=1), else 0

        resIdx = 0
        resLen = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right-left+1
                    resIdx = left
                right += 1
                left -= 1
            
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right-left+1
                    resIdx = left
                right+= 1
                left -= 1

        return s[resIdx: resIdx+resLen]





