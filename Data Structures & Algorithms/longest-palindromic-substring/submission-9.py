class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Let T(i,j) = True if the substring from i to j is a substring and False otherwise
        #Recursive: T(i,j) = (s[i]==s[j]^T(i-1, j+1))
        dp = {}
        def backtrace(left, right):
            if left >= right:
                return True
            if (left,right) in dp:
                return dp[(left,right)]
            if s[left] != s[right]:
                dp[(left, right)] = False
                return dp[(left, right)]
            #only leaves the case where left and right are equal to each other
            dp[(left, right)] = backtrace(left + 1, right - 1)
            return dp[(left,right)]


        final_left = 0
        final_right = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                if backtrace(left, right):
                    if right - left > final_right - final_left:
                        final_left = left
                        final_right = right

        return s[final_left:final_right + 1]

            
        