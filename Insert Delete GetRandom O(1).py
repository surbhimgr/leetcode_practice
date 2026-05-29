'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Solution - 
Maintain a list and a dictionary of positions for running insert and remove in O(1) time.
Randomized function explicitely mentions the elemnts should've equal probability of bieng returned i.e. uniform probability so we cant just return any element thing its just random as it wont follow uniform probability.
As it is testing if there are 3 elements in the list and function has been called 1000 times and all 3 elements must have been returned 1/3rd of time.
'''

import random
class RandomizedSet:

    def __init__(self): #O(1)
        self.randomSet=[]
        self.pos={}

    def insert(self, val: int) -> bool: #O(1)
        if val in self.pos:
            return False
        self.pos[val]=len(self.randomSet)
        self.randomSet.append(val)
        return True

    def remove(self, val: int) -> bool: #O(1)
        if val not in self.pos:
            return False
        index = self.pos[val]
        last_element = self.randomSet[-1]   
        #swap with last element
        self.randomSet[index] = last_element
        self.pos[last_element] = index 
        #remove last
        self.randomSet.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int: #O(1)
        return random.choice(self.randomSet)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
