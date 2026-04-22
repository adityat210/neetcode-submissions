class Solution:
    def countSubstrings(self, s: str) -> int:
        #return the number of substrings within s that are palindromes
        total = 0
        dp = {}
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left-=1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
        return total

        