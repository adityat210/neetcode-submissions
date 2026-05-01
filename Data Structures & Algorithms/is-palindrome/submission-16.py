class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers
        #initalize at 0 and end of str
        l, r = 0, len(s)-1
        #while l is a lower index than r, ensures that the two don't overlap
        while l < r:
            #while l is less than r and still not an alpha numeric 
            while l<r and not self.alphaNum(s[l]):
                #increase l
                l += 1
            #while r is more than l and r is still not alpha numeric
            while l<r and not self.alphaNum(s[r]):
                #reduce r 
                r -= 1
            #if the letters when found arent the same, case-insensitive, return false
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return (ord("A")<= ord(c)<=ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

