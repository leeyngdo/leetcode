class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = dict()
        freq_t = dict()

        if len(s) != len(t):
            return False

        for x, y in zip(s, t):
            freq_s[x] = freq_s.get(x, 0) + 1
            freq_t[y] = freq_t.get(y, 0) + 1

        while freq_s:
            key, val = freq_s.popitem()
            if not (key in freq_t) or val != freq_t[key]:
                return False
            
        return True
