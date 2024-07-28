class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        maximum = cur
        for i in range(k, len(nums)):
            cur = cur +nums[i] - nums[i-k]
            maximum = max(maximum, cur)
        max_ave = maximum/k
        return max_ave
        
        