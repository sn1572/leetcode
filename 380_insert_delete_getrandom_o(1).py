import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = {}
        self.length = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.storage:
            return(False)
        self.storage[val] = 0
        self.length += 1
        return(True)
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.storage:
            del self.storage[val]
            self.length -= 1
            return(True)
        return(False)
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0,self.length-1)
        keys = list(self.storage.keys())
        return(keys[index])


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()