class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * len(nums)
        if k ==0:
            return nums
        
        if 2 * k + 1 > len(nums):
            return result
        summ = sum(nums[:2 * k + 1])
        result[k] = summ //(2 * k + 1)
        for i in range(2 * k + 1, len(nums)):
            summ = summ + nums[i] -nums[i - (2*k+1)]
            result[i-k] = summ // (2*k+1)
        return result
