class Solution:
    # @lru_cache(None)
    def __init__(self):
        self.memo = {}
    
    def fib(self, n: int) -> int:
        if n <= 1: return n
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fib(n-2) + self.fib(n-1)
        return self.memo[n]
        # if n <= 1: return n
        # return self.fib(n-2) + self.fib(n-1)
    
        
         
        