class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 4: return 1
        
        lo = 0; hi = len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            a = True if mid == 0 else arr[mid - 1] < arr[mid]
            b = True if mid == len(arr) - 1 else arr[mid] < arr[mid + 1]
            if a and b:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
            