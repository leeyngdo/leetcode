class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        
        lo = 0; hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[0]:
              lo = mid + 1
            elif nums[mid] < nums[0]:
              hi = mid
            else:
              if nums[hi] >= nums[hi - 1]: hi -= 1
              else: lo += 1
        
        k = 0 if nums[lo] > nums[0] else lo
        return nums[k]