from linkedlistiterator import LinkedListIterator
class LinkedClass:
    def __init__(self):
        self._theItems =set()
    def adding(self,item):
        self._theItems.add(item)
    def delete(self,item):
        self._theItems.remove(item)
    def len(self):
        return len(self._theItems)
    def __iter__(self):
        return next (self._theItems) 
    def uni(self,item):
        return self._theItems.union(item)
    def inter(self,item):
        return self._theItems.intersection(item)
    def subs(self,item):
        return self._theItems.issubset(item)
    def eq(self,item):
        return self._theItems.equals(item)
"""
odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])
print(odds.union(evens))
print(odds)
print(evens)
print(odds.intersection(primes))
print(evens.intersection(primes))
print(odds.intersection(evens))
print(composites.union(primes))
print(2 in primes)
print(9 not in evens)
"""
