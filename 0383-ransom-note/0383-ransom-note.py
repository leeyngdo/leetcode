class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        hash_table = {}
        for letter in magazine:
            hash_table[letter] = hash_table.get(letter, 0) + 1
        
        for letter in ransomNote:
            if not letter in hash_table:
                return False
            else:
                hash_table[letter] -= 1
                if hash_table[letter] == 0:
                    del hash_table[letter]
        
        return True