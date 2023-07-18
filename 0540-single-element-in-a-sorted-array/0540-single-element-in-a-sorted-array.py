class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return nums[0]

        lo = 0; hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            tmp_1 = mid % 2 == 0 and nums[mid] == nums[mid + 1]
            tmp_2 = mid % 2 == 1 and nums[mid] == nums[mid - 1]

            if tmp_1 or tmp_2: # Then the answer is on the right subarray
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]
