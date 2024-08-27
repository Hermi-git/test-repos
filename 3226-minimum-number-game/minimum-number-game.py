class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            result.append(nums[i])
        for i in range(0, len(nums), 2):
            result[i], result[i+1] = result[i+1], result[i]
        return result