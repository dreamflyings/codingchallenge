"""
https://leetcode.com/problems/merge-intervals/description/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

---

This one took some time to get correct. Inspiration had to be found from the
discussion forum.

Key insight is to maintain a second list for merged results. The last element
of the merged list is modified as we iterate the intervals.

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

    def merge(self, intervals):
        intervals.sort(key=lambda i: i.start)

        l = len(intervals)
        if l == 0:
            return []
        elif l == 1:
            return intervals

        merged = []
        merged.append(intervals[0])

        for i in intervals:
            prev = merged[-1]
            curr = i

            if prev.end < curr.start:
                # normal case
                merged.append(curr)
            else:
                start = prev.start
                end = max(prev.end, curr.end)
                merged[-1] = Interval(start, end)

        return merged
