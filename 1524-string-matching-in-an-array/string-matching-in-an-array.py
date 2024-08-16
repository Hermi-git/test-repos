class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j]:
                    if re.search(re.escape(words[i]) , words[j]) and words[i] not in matches:
                        matches.append(words[i])
        return matches

        
        