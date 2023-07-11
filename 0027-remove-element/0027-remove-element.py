class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0; k = len(nums)
        
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                k -= 1
            else:
                i += 1

        return k