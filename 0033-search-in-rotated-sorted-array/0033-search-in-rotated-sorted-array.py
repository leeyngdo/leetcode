class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        # Find a boundary point
        lo = 0; hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid
        k = 0 if nums[0] < nums[lo] else len(nums) - lo
        print(k)
        # Binary Search        
        lo = 0; hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid - k] < target:
                lo = mid + 1 
            else:
                hi = mid
                
        if nums[lo - k] != target: return -1

        return lo - k if lo >= k else len(nums) + lo - k
                