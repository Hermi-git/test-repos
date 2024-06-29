class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
        total_result = 0
        for i in range(len(s)):
            current_value = roman_to_integer[s[i]]
            if i+1<len(s) and roman_to_integer[s[i + 1]] > current_value:
                total_result -= current_value
            else:
                total_result += current_value
        return total_result


        