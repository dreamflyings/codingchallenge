"""
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?

---

Iteratively

Input: 1->2->3->4->5->NULL

Initial:
curr = 1
next = None
prev = None

while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

return prev

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        next = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
