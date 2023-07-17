class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        
        lo = 0; hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid 
                
        k = 0 if nums[lo] >= nums[0] else lo
        
        return nums[k]