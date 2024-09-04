class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {num:i for i, num in enumerate(nums1)}
        stack = []
        result = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                value = stack.pop()
                idx = nums1_dict[value]
                result[idx] = nums2[i]
            if nums2[i] in nums1_dict:
                stack.append(nums2[i])
        return result
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # nums1_dict = {}
        # for index, num in enumerate(nums1):
        #     nums1_dict[num] = index
        # result =[-1] * len(nums1)
        # stack = []
        # for i in range(len(nums2)):
        #     while stack and stack[-1] < nums2[i]:
        #         val = stack.pop()
        #         idx = nums1_dict[val]
        #         result[idx] = nums2[i]
        #     if nums2[i] in nums1_dict:
        #         stack.append(nums2[i])
        # return result

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        

                
            

       