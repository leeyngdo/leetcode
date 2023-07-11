class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        idx1 = idx2 = 0

        ret = ""
        while True:
            if idx1 <= len(word1) - 1 and idx2 <= len(word2) - 1:
                ret += word1[idx1] + word2[idx2]
                idx1 += 1; idx2+= 1
            elif idx1 <= len(word1) - 1:
                ret += word1[idx1:]
                return ret
            elif idx2 <= len(word2) - 1:
                ret += word2[idx2:]
                return ret
            else:
                return ret