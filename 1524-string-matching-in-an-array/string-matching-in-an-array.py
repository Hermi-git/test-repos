class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        matches = set()
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if re.search(re.escape(words[i]) , words[j]):
                    matches.add(words[i])
                    break
        return list(matches)

        
        