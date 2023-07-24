class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        arr = sorted([(x, j) for j, x in enumerate(intervals)])
        for i in range(len(intervals)):
            target = intervals[i][1]
            lo = 0; hi = len(arr) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid][0][0] < target:
                    lo = mid + 1
                else:
                    hi = mid

            if arr[lo][0][0] < target:
                ans.append(-1)
            else:
                ans.append(arr[lo][1])

        return ans