class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bdry = bisect.bisect_left(nums, 0)
        pos = nums[bdry:]; neg = nums[:bdry]
        i = len(neg) - 1; j = 0
        ans = []
        while i >= 0 and j <= len(pos) - 1:
            a = neg[i] ** 2; b = pos[j] ** 2
            if a > b:
                ans.append(b)
                j += 1
            else:
                ans.append(a)
                i -= 1

        if i >= 0:
            while i >= 0:
                ans.append(neg[i] ** 2)
                i -= 1
        if j <= len(pos) - 1:
             while j <= len(pos) - 1:
                ans.append(pos[j] ** 2)
                j += 1
            
        return ans