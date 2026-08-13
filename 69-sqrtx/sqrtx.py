class Solution:
    def mySqrt(self, x: int) -> int:
        if 0<x<2:
            return 1
        left,right =2,x//2
        ans=0
        while left<=right:
            mid = left+(right-left)//2
            num =mid*mid
            if num==x:
                return mid
            elif num<x:
                ans  = mid
                left=mid+1
            else:
                right=mid-1
        return right

        