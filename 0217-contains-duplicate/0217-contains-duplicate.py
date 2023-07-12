class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_table = {}
        for num in nums:
            if num in hash_table:
                return True
            else:
                hash_table[num] = True
        return False
