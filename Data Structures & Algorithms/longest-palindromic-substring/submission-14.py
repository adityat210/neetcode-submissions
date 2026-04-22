class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Let T(i, j) = the longest substring of s[i...j] that is a palindrome
        #Recursive:  T(i,j) = 
            #1 if i = j
            #1 if s[i] = s[j] and T(i+1, j-1) = 1
            #1 if j-i = 1

        #T(i,j)=whether substring s[i..j] is a palindrome
        #T(i,j)=1 if s[i]=s[j] and (j−i≤2 or T(i+1,j−1)=1), else 0

        resIdx, resLen = 0,0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i+1):
                        resIdx = i
                        resLen = j-i+1
        return s[resIdx: resIdx+resLen]