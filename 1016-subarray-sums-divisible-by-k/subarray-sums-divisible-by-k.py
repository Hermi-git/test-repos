class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        px_dict = {}
        px_dict[0] = 1
        running = 0
        count = 0
        for i in range(len(nums)):
            running += nums[i]
            remainder = running % k
            if remainder < 0:
                remainder += k
            count += px_dict.get(remainder,0)
            px_dict[remainder ] = px_dict.get(remainder , 0)+ 1
        return count
        
       