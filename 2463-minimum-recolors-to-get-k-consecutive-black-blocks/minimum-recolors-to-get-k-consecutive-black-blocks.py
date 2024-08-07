class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current = sum(1 for i in blocks[:k] if i == "W")
        result = current
       
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                current += 1
            if blocks[i - k] == "W":
                current -= 1
            result = min(result, current)
        
        return result
        
