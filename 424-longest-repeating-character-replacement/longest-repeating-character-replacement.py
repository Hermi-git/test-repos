class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_count =Counter()
        l = 0
        longest = 0
        max_count = 0
        for r in range(len(s)):
            s_count[s[r]] += 1
            max_count = max(max_count, s_count[s[r]])
            changed = (r - l + 1) - max_count

            if changed > k:
                s_count[s[l]] -= 1
                l += 1
        
        longest =max(longest, r - l + 1)
        return longest

        


        
        
        