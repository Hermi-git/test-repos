class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        small_count ={}
        for index, item in enumerate(arr):
            if item not in small_count:
                small_count[item] = index
        result=[]
        for item in nums:
            result.append(small_count[item])
        return result

        