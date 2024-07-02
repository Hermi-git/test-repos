class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        num1, num2 =0,0
        result= []
        while num1 < len(nums1) and num2 < len(nums2):
            if nums1[num1] == nums2[num2]:
                result.append(nums1[num1])
                num1 += 1
                num2 += 1
            elif nums1[num1] < nums2[num2]:
                num1 += 1
            else:
                num2 += 1
        return result