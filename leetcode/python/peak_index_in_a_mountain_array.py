"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

Let's call an array A a mountain if the following properties hold:

* A.length >= 3

* There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] <
  A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] <
A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1

Example 2:

Input: [0,2,1,0]
Output: 1

Note:

* 3 <= A.length <= 10000
* 0 <= A[i] <= 10^6
* A is a mountain, as defined above.

---

[0, 1, 0]

i b f
1 0 1
2 1 0 b<f,

[0, 1, 2, 0]

i b f
1 0 1
2 1 2
3 2 0 # is peak

[0, 2, 1, 0]

i b f
1 0 2
2 2 1 # peak?
3 1 0



"""


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)

        if l in set([0, 1, 2]):
            return 0

        max_peak = -1
        index = None

        for i in range(1, l):
            b = A[i - 1]  # back
            f = A[i]  # front

            if f < b and f > max_peak:
                max_peak = f
                index = i - 1

        return index
