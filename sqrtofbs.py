#sqrt using binary search
class Solution(object):
    def mySqrt(self, n):
        """
        :type x: int
        :rtype: int
        """
        if n==0:
            return 0
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                low=mid+1
            else:
                high=mid-1
        return high
