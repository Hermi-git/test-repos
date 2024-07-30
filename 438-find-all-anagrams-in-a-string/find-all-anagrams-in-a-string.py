class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount = Counter(p)
        result = []
        current = Counter(s[:len(p)])
        if current == pCount:
            result.append(0)
        for i in range(len(s)-len(p)):
            current[s[i]] -= 1
            current[s[i + len(p)]] += 1
            if current == pCount:
                result.append(i+1)
        return result  




        


        

        