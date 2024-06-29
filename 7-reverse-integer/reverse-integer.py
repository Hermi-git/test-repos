class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = x*sign
        str_x = str(x)
        reversed_x = int(str_x[::-1]) * sign
        if reversed_x < -2**31 or reversed_x > 2**31-1:
            return 0
        return reversed_x
        