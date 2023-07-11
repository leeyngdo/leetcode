class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0; fast = 1; k = len(nums)
        
        chance = True
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                if not chance:
                    nums.pop(fast)
                    k -= 1
                else: 
                    chance = False
                    slow = fast; fast += 1
            else:
                chance = True
                slow = fast; fast += 1
                
        return k