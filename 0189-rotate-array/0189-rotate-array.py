class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        save = []; k = k % len(nums)
        if k == 0:
            return nums
        save[:len(nums) - k] = nums[:-k]
        
        for i in range(len(nums)):
            if i < k:
                nums[i] = nums[len(nums) - k + i]
            else:
                nums[i] = save[i - k]