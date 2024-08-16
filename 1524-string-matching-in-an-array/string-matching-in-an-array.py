class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        matches = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if re.search(re.escape(words[i]) , words[j]) and words[i] not in matches:
                    matches.append(words[i])
                    break
        return matches

        
        