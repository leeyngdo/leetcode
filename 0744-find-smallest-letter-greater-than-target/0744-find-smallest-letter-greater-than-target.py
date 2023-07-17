class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        lo = 0; hi = len(letters) - 1
        
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if letters[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        
        if hi == len(letters) - 1:
            return letters[0]
        if lo == 0 and target < letters[lo]:
            return letters[0]
        
        return letters[lo + 1]
        
