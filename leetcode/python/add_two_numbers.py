"""
### Problem ###
https://leetcode.com/problems/add-two-numbers/description/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

### Notes ###

Many corner cases here work them one at a time.  Not too difficult.

"""

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbersTest(unittest.TestCase):
    def add_two_numbers(self, l1, l2):
        n1 = l1
        n2 = l2

        first = None
        node = None

        carry = 0

        while n1 is not None or n2 is not None or carry != 0:
            v1 = n1.val if n1 is not None else 0
            v2 = n2.val if n2 is not None else 0

            s = v1 + v2 + carry
            if s > 9:
                carry = 1
                s = s - 10
            else:
                carry = 0

            n = ListNode(s)

            if first is None:
                first = n
                node = n
            else:
                node.next = n
                node = n

            n1 = n1.next if n1 is not None else n1
            n2 = n2.next if n2 is not None else n2

        return first

    def num_to_linked_list(self, x):
        last = None
        for x in reversed(list(str(x))):
            n = ListNode(int(x))
            if last is not None:
                n.next = last
            last = n
        return last

    def print_linked_list(self, x):
        result = []
        node = x
        while node is not None:
            result.append(node.val)
            node = node.next
        return int("".join(map(lambda x: str(x), result)))

    def test_example_1(self):
        l1 = self.num_to_linked_list(243)
        l2 = self.num_to_linked_list(564)
        result = self.add_two_numbers(l1, l2)
        expected = 708
        actual = self.print_linked_list(result)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        l1 = self.num_to_linked_list(5)
        l2 = self.num_to_linked_list(5)
        result = self.add_two_numbers(l1, l2)
        expected = 1
        actual = self.print_linked_list(result)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        # 9 + 9 = 18
        l1 = self.num_to_linked_list(9)
        l2 = self.num_to_linked_list(9)
        result = self.add_two_numbers(l1, l2)
        expected = 81
        actual = self.print_linked_list(result)
        self.assertEqual(expected, actual)

    def test_example_4(self):
        # 81 + 0 = 81
        l1 = self.num_to_linked_list(18)
        l2 = self.num_to_linked_list(0)

        result = self.add_two_numbers(l1, l2)
        expected = 18
        actual = self.print_linked_list(result)
        self.assertEqual(expected, actual)
