class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, num in enumerate(nums):
            d_num = target - num
            if d_num in mapping:
                return [mapping[d_num], index]
            mapping[num] = index
        return []
        