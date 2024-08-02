class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r =0, 0
        sum = 0
        nums_set = set()
        cur_sum = 0
        max_sum = 0
        while r < len(nums):
            while nums[r] in nums_set:
                nums_set.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            nums_set.add(nums[r])
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
            r += 1
           
        return max_sum


        