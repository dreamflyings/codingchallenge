"""
# https://leetcode.com/problems/peeking-iterator/description/

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
---

This appears to be straightforward.

It seems like I would maintain my own FIFO.

removed from head <-- 0 1 2 3 <-- added to tail

"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.q = []

    def empty(self):
        return len(self.q) == 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.it.hasNext():
            self.q.append(self.it.next())

        return self.q[0]  # TODO: throw exception if q empty

    def next(self):
        """
        :rtype: int
        """
        if self.empty():
            return self.it.next()
        else:
            x = self.q[0]
            self.q = self.q[1:]
            return x

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.empty():
            return self.it.hasNext()
        else:
            return True


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
