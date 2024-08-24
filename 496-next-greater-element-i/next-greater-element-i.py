class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {num:index for index, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                idx = nums1_dict[val]
                result[idx] = nums2[i]
            if nums2[i] in  nums1_dict:
                stack.append(nums2[i])
        return result

        

                
            

       