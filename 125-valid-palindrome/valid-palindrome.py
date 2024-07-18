class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s = ''.join(char for char in s.lower() if char.isalnum())
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        