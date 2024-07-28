class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r =0 , 0
        maximum = 0
        s_set = set()
        while r < len(s):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            r += 1
            maximum = max(maximum, r - l)
        return maximum
        

        
        