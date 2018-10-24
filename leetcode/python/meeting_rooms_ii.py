"""
https://leetcode.com/problems/meeting-rooms-ii/description/

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

Example 1:

Input: [[0, 30],[5, 10], [15, 20]]
Output: 2

starts = 0,  5,  15
ends   = 10, 20, 30

s[0]=0  < e[0]=10 --> rooms++
s[1]=5  < e[0]=10 --> rooms++
s[2]=15 > e[0]=10 -->

---

Example 2:

Input: [[7,10],[2,4]]
Output: 1

---

This seems to be a variant of the merged interval problem.

Number of times you merge is number of unique conference rooms.

Example 3:

[[9,10],[4,9],[4,17]]

[[4,9],[4,17],[9,10]]

Hint: consider the room as resource?

starts = [4,4,9]
ends   = [9,10,17]

start 4, ends[0]=9 no room avail, rooms+=1
start 4, ends[0]=9 no room avail, rooms+=1
start 9, ends[9]=9 room avail

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        l = len(intervals)
        if l in set([0, 1]):
            return l

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        rooms = 0

        si = 0
        ei = 0

        while si < l:
            s = starts[si]
            e = ends[ei]

            if s < e:
                rooms += 1
            else:
                ei += 1

            si += 1

        return rooms
