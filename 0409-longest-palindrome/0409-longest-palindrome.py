class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = dict(); out = 0; one_letter = False
        for letter in s: 
            hash_table[letter] = hash_table.get(letter, 0) + 1
            if hash_table[letter] >= 2: 
                out += 2; hash_table[letter] -= 2
        if 1 in hash_table.values(): out += 1
            
        return out
