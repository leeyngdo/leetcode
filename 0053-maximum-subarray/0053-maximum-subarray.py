class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        l = r = 0
        max_sum = current_sum = nums[0]
        while r <= len(nums) - 1:
            if r != l: current_sum += nums[r]
            
            max_sum = max(max_sum, current_sum)
            if current_sum > 0:
                r += 1
            else:
                if l == r: r += 1
                l = r
                if l <= len(nums) - 1:
                    current_sum = nums[l]
        return max_sum
            