import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}
        self.order = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.cache:
            return False
        
        self.order.append(val)
        self.cache[val] = len(self.order) -1 
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.cache:
            return False
        
        index = self.cache[val]
        self.cache[self.order[len(self.order)-1]] = index
        del(self.cache[val])
        self.order[index], self.order[len(self.order)-1] = self.order[len(self.order)-1], self.order[index]
        self.order.pop()
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand = random.randint(0, len(self.order)-1)
        return self.order[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()