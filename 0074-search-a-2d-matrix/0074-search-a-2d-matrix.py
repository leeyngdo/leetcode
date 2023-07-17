class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix); n = len(matrix[0])

        if target < matrix[0][0] or target > matrix[m - 1][n - 1]: return False

        lo = 0; hi = m * n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            mid_h = mid // n; mid_v = mid % n
            if matrix[mid_h][mid_v] < target:
                lo = mid + 1
            else:
                hi = mid
        
        return True if matrix[lo // n][lo % n] == target else False