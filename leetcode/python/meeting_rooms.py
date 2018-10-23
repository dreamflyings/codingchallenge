"""
https://leetcode.com/problems/meeting-rooms/description/

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true

---

1. Use brute force to check intersection between pairs of meeting times O(n^2)
2. Sort by start time. Does next meeting start before current meeting ends?

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """

        meetings = len(intervals)

        if meetings in set([0, 1]):
            return True

        intervals.sort(key=lambda i: i.start)

        i = 1

        while i < meetings:
            prev = intervals[i - 1]
            curr = intervals[i]

            if prev.end > curr.start:
                return False
            i += 1

        return True
