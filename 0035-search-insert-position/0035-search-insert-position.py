class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0; hi = len(nums) - 1
        if lo == hi:
            if nums[lo] == target: return 0
            else: return int(nums[lo] < target)
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                hi = mid - 1
        
        return lo