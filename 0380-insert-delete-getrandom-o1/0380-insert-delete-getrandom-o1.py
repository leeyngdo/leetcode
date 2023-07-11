class RandomizedSet(object):

    def __init__(self):
        self.dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        else:
            self.dict[val] = True
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            del self.dict[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.dict.keys())
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()