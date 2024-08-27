class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre_prod =1
        for i in range(len(nums)):
            answer[i] = pre_prod
            pre_prod *= nums[i]
        post_prod = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= post_prod
            post_prod *= nums[i]
        return answer



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       

        