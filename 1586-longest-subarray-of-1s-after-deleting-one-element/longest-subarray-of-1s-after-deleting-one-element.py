class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones = 0
        cnt_zero = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt_zero += 1
            
            while cnt_zero > 1:
                if nums[l] == 0:
                    cnt_zero -= 1
                l += 1
            max_ones = max(max_ones, r-l)
        return max_ones
        

            
       
        