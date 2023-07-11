class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = dict() # key: number / value: index
        for idx, val in enumerate(numbers):
            remain = target - val

            if remain in seen: # O(1)
                return [min(idx, seen[remain]) + 1, max(idx, seen[remain]) + 1]
            
            seen[val] = idx