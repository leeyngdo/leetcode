class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if arr[0] - 1 >= k: return k

        lo = 0; hi = len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if arr[mid] - mid - 1 >= k:
                hi = mid - 1
            else:
                lo = mid
        return arr[lo] + k - (arr[lo] - lo - 1)