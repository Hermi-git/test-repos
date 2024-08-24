class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        update = [0] * len(s)
        for start, end, direction in shifts:
            update[start] += 1 if direction == 1 else -1
            if end < len(s) -1:
                update[end + 1] += 1 if direction == 0 else -1
        for i in range(1, len(update)):
            update[i] += update[i-1]
        result = ""
        for i in range(len(update)):
            result += chr(((ord(s[i]) - ord('a') + update[i]) % 26 )+ ord('a'))
        return result


       