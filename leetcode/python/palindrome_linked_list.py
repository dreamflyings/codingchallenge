"""
https://leetcode.com/problems/palindrome-linked-list/description/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

---

Use stack

Find tail
Find middle
reverse middle to tail
iterate head -> middle and tail -> middle, check if val is equal

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #        stack = []
        #
        #        node = head
        #        while node is not None:
        #            stack.append(node.val)
        #
        #        node = head
        #        while node is not None:
        #            if stack[-1] != node.val:
        #                return False
        #            stack = stack[:-1]
        #
        #        return True

        if not head: return True

        # Locate tail
        node = head
        size = 0
        while node is not None:
            tail = node
            size += 1
            node = node.next
        #print(tail.val, size, int(size/2))

        # Locate middle
        i = 0
        node = head
        while i < int(size / 2):
            i += 1
            node = node.next
        middle = node
        print(middle.val, size)

        if size == 1:
            return True
        elif size == 2:
            return head.val == middle.val

        # Reverse from middle
        node = middle
        curr = node
        next = None
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Iterate inwards
        while head is not None and tail is not None:
            if head.val != tail.val:
                return False

            head = head.next
            tail = tail.next

        return True
