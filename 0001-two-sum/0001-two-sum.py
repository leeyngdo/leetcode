class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = dict() # key: number / value: index
        for idx, val in enumerate(nums):
            remain = target - val

            if remain in seen: # O(1)
                return [idx, seen[remain]]
            
            seen[val] = idx