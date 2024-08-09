class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        nums_dict = {}
        nums_dict[0] = 1
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remaining = prefix_sum - k
            count += nums_dict.get(remaining, 0)
            nums_dict[prefix_sum] = nums_dict.get(prefix_sum, 0)+1
        return count

        