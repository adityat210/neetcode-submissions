class Solution:
    def numDecodings(self, s: str) -> int:
        #T(i) = the number of possible ways to decode the string s[1..i]
        #Recursive: T(i) = T(i-2) * decode(s[i-1...i]) + T(i-1) * decode(s[i])

        #need to check if selected string is decodable
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]

            if i >= 2 and 10 <= int(s[i-2:i])<=26:
                dp[i] += dp[i-2]

        return dp[n]
