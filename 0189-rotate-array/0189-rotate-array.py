class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        front = []; behind = []; k = k % len(nums)

        for _ in range(k):
            front.append(nums.pop())
        while nums:
            behind.append(nums.pop())

        while front:
            nums.append(front.pop())
        while behind:
            nums.append(behind.pop())