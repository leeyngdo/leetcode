class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0] or len(arr) < k-1: return arr[:k]
        if x >= arr[-1]: return arr[-k:]

        lo = 0; hi = len(arr) - k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid

        return arr[lo:lo+k]
        