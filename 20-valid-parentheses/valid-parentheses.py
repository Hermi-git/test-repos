class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "}":"{", "]":"["}
        for bracket in s:
            if bracket in dict.values():
                stack.append(bracket)
            else:
                if len(stack) != 0 and stack[-1] == dict[bracket]:
                    stack.pop()
                else:
                    return False
        return len(stack) ==0
    
                    
        