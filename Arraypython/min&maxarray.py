#find the min max of an array
'''class Solution(object):
    def findMin(self, numsc):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(numsc)-1
        while low<high:
            mid=(low+high)//2
            if numsc[mid]>numsc[high]:
                low=mid+1
            else:
                high=mid
        return numsc[low]
        '''
#maximum in rotated sorted array
'''
class Solution(object):
    def findMax(self, nums):
        low = 0
        high = len(nums) - 1
        if nums[low] <= nums[high]:
            return nums[high]
        while low <= high:
            mid = (low + high) // 2
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid]
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid - 1]
            if nums[mid] > nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]
        '''