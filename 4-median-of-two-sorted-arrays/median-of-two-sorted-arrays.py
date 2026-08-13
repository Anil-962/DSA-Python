class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        A= nums1
        B = nums2
        m=len(A)
        n = len(B)
        left =0
        right = m
        half = (m+n+1)//2
        while left<=right:
            PA = (right+left)//2
            PB = half-PA
            if PA ==0:
                Aleft = float('-inf')
            else:
                Aleft  = A[PA-1]
            if PA ==m:
                Aright =float('inf')
            else:
                Aright = A[PA]
            if PB ==0:
                Bleft =float('-inf')
            else:
                Bleft = B[PB-1]
            if PB==n:
                Bright =float('inf')
            else: 
                Bright = B[PB]
            if Aleft<=Bright and Bleft<=Aright:
                if (m+n)%2==1:
                    return max(Aleft,Bleft)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2.0
            elif Aleft>Bright:
                right = PA-1
            else:
                left = PA+1
        