# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None: 
            return False

        tail = head
        head = tail.next

        while tail != None and head != None and head.next != None:
            if tail == head:
                return True
            tail = tail.next
            head = head.next.next

        return False

