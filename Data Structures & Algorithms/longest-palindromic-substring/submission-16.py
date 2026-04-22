class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Let T(i, j) = the longest substring of s[i...j] that is a palindrome
        #Recursive:  T(i,j) = 
            #1 if i = j
            #1 if s[i] = s[j] and T(i+1, j-1) = 1
            #1 if j-i = 1

        #T(i,j)=whether substring s[i..j] is a palindrome
        #T(i,j)=1 if s[i]=s[j] and (j−i≤2 or T(i+1,j−1)=1), else 0

        #return the length of the maximum substring that is a palindrome
        #Let T(i,j) = the longest substring from s[i] to s[j] that is a palindrome

        #dp would require O(n^2)
        #two pointer would allow for O(1)

        final_i = 0
        final_length = 0
        for i in range(len(s)):
            #odd length palindromic substrings
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > final_length:
                    final_i = left
                    final_length = right - left + 1
                left -= 1
                right += 1
            
            #even length palindromic. substrings
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > final_length:
                    final_i = left
                    final_length = right- left + 1
                left -= 1
                right += 1

        return s[final_i: final_i + final_length]
            
