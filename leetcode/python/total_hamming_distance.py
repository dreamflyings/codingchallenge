"""
### Problem ###

https://leetcode.com/problems/total-hamming-distance/description/

Input: 4, 14, 2

Output: 6

### Notes ###

Recall:

- Number of permutations (order matters) of n objects: n!
- Number of ordered samples of size r, with replacement, from n objects: n^r
- Number of ordered samples of size r, without replacement, from n objects: n!/(n-r)!

- Number of unordered samples size r, without replacements (combinations)

n!/(r!*(n-r)!) = 6/(2) = 3

What is runtime complexity? --> O(n!)


Argh, I need a hint!

0100 ^ 1110 ^ 0010 = 1000 = 8? nope

hint: num0s*num1s for each bit and sum

4 ->  0100
14 -> 1110
2 ->  0010

i num0s num1s num0s*num1s
0 2     1     2
1 1     2     2
2 1     2     2
3 3     0     0
sum           6

Now, work through algorithm ...

"""

import unittest


class TotalHammingDistanceTest(unittest.TestCase):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n!)
        # return sum(map(lambda x: self.hammingDistance(x[0], x[1]), itertools.combinations(nums, 2)))

        nums_count = len(nums)

        distance = 0

        for bit in range(4):  # FIXME
            num_0s = 0
            num_1s = 0

            count_me = []

            for num in nums:
                x = 1 if num & (1 << bit) else 0
                count_me.append(x)

            num_1s = sum(filter(lambda x: x == 1, count_me))
            num_0s = nums_count - num_1s

            distance += num_0s * num_1s

        return distance

    def test_smoke(self):
        self.assertEqual(6, self.totalHammingDistance([4, 14, 2]))
        self.assertEqual(7, self.totalHammingDistance([1337, 7331]))
