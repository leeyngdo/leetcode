class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or nums[0] > target or nums[len(nums) - 1] < target:
            return [-1, -1]

        lo_1 = 0; hi_1 = len(nums) - 1
        lo_2 = 0; hi_2 = len(nums) - 1
        while lo_1 < hi_1 or lo_2 < hi_2:
            if lo_1 != hi_1:
                mid_1 = lo_1 + (hi_1 - lo_1)//2
                if nums[mid_1] < target:
                    lo_1 = mid_1 + 1
                else:
                    hi_1 = mid_1
                
            if lo_2 != hi_2:
                mid_2 = lo_2 + (hi_2 - lo_2 + 1)//2
                if nums[mid_2] > target:
                    hi_2 = mid_2 - 1
                else:
                    lo_2 = mid_2

        if nums[lo_1] != target and nums[lo_2] != target:
            return [-1, -1]
        return [lo_1, lo_2]