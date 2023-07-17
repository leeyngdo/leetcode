class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0] or target > nums[len(nums) - 1]: return -1
        
        lo = 0; hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
            
        return lo if nums[lo] == target else -1