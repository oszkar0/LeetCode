import random

class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.index_map = {}

    def search(self, val):
        return val in self.index_map
    
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.search(val):
            return False
        
        self.list.append(val)
        self.index_map[val] = len(self.list) - 1
        return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.index_map:
            return False

        index = self.index_map[val]
        self.list[index] = self.list[-1]
        self.index_map[self.list[-1]] = index
        self.list.pop()
        del self.index_map[val]
        return True

        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()