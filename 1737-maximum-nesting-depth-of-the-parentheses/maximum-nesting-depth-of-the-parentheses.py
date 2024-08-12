class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth =0
        cur_depth = 0
        for c in s:
            if c == "(": 
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)  
            elif c == ")":  
                cur_depth -= 1
        
        return max_depth
        
        
        