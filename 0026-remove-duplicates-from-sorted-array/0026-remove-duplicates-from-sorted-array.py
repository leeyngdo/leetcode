class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0; fast = 1; k = len(nums)
        
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                nums.pop(fast)
                k -= 1
            else:
                slow = fast
                fast += 1
                
        return k