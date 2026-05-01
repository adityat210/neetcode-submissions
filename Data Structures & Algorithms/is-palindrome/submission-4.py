class Solution:
    def isPalindrome(self, s: str) -> bool:
        #need to make the string case insensitive
        #can iterate over the new string without spaces or special characters
        newString = ""
        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]