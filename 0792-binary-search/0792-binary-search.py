class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = ans = len(nums) // 2

        while True:
            if not nums:
                return - 1

            pivot = nums[idx]
            if pivot > target:
                nums = nums[:idx]
                idx = len(nums) // 2; ans -= len(nums) - idx
            elif pivot < target:
                nums = nums[idx + 1:]
                idx = len(nums) // 2; ans += idx + 1
            else:
                return ans