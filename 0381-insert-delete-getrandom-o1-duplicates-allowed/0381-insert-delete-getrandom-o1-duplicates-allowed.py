class RandomizedCollection(object):

    def __init__(self):
        self.data_idx = {}
        self.data = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        self.data.append(val)

        if val in self.data_idx:
            self.data_idx[val].add(len(self.data) - 1)
            return False
        else:
            self.data_idx[val] = set({len(self.data) - 1})
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # If val is not inserted, return false.
        if not val in self.data_idx:
            return False
        
        # Choose random index of val.
        remove_idx = self.data_idx[val].pop()
        if not self.data_idx[val]:
            del self.data_idx[val]

        # It fills the removed index with the last inserted element.
        if remove_idx != len(self.data) - 1:
            last = self.data[-1]
            self.data[remove_idx] = last
            self.data_idx[last].remove(len(self.data) - 1)
            self.data_idx[last].add(remove_idx)

        self.data.pop()
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()