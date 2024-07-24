class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        min_length = float("inf")
        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum >= target:
                current_sum -= nums[start]
                min_length = min(min_length, end - start+1)
                start +=1 
        if min_length != float("inf"):
            return min_length
        else:
            return 0


        