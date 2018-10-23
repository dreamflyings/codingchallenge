"""
### Problem ###

https://leetcode.com/problems/queue-reconstruction-by-height/description/

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:

The number of people is less than 1,100.


### Notes ###

The solution is not immediate to me.  I needed hints, it was helpful to learn about queue.insert.  I better understand
now.

"""

import unittest


class QueueReconstructionByHeightTest(unittest.TestCase):
    def reconstructQueue(self, people):
        # tall to short with increasing k value
        people_by_height = sorted(
            people, key=lambda x: (-x[0], x[1]))  # wow, you can return tuple
        # print("people_by_height")
        # print(people_by_height)

        queue = []
        for p in people_by_height:
            height = p[1]
            queue.insert(height, p)
            # print(p, "@", height, "->", queue)
        # print("queue")
        # print(queue)
        return queue

    def test_basic(self):
        input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        self.assertEqual(expected, self.reconstructQueue(input))
