class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=len(nums1)
        b=len(nums2)
        c=[]
        if(a<=b):
            for i in nums1:
                if(i in nums2):
                    c.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if(i in nums1) :
                    c.append(i)
                    nums1.remove(i)
        return c
