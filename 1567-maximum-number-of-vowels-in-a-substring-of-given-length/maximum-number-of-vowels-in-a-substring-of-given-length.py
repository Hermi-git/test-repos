class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiouAEIOU")
        current = sum(1 for i in s[:k] if i in vowels)
        maximum = current
        for i in range(k, len(s)):
            if s[i] in vowels:
                current += 1
            if s[i-k] in vowels:
                current -= 1
            maximum = max(maximum, current)
        return maximum


        
        