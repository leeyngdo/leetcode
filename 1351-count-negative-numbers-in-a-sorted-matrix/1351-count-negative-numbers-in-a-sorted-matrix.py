class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid); n = len(grid[0])
        if grid[m-1][n-1] >= 0: return 0
        ans = 0
        for i in range(m):
            target = grid[i]
            lo = 0; hi = n - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if target[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid - 1
            ans += n - lo

        return ans