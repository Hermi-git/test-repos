class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            i = i % n
            while stack and nums[stack[-1]] < nums[i]:
                val = stack.pop()
                result[val] = nums[i] 
            stack.append(i)
        return result
               
      
       
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
       