class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack =[]
        for i in range(2 * n):
            i = i % n
            while stack and nums[stack[-1]] < nums[i]:
                value =stack.pop()
                result[value] = nums[i]
            if i < n:
                stack.append(i)
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # result = [-1] * n
        # stack = []
        # for i in range(2 * n):
        #     index = i % n
        #     while stack and nums[stack[-1]] < nums[index]:
        #         prev_index = stack.pop()
        #         result[prev_index] = nums[index]
        #     if i < n:
        #         stack.append(index)
        # return result
               
      
       
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
       