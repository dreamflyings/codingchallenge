"""
https://leetcode.com/problems/merge-k-sorted-lists/description/

---

Iterate on heads of each list. Find min. Create new list.

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]

Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)

        head = None
        tail = None

        done = False

        while not done:
            mins = []
            for i in range(k):
                if lists[i]:
                    mins.append((lists[i].val, i))

            if len(mins) != 0:
                min_val = sys.maxsize
                k_idx = None

                for i in range(len(mins)):
                    if mins[i][0] < min_val:
                        min_val = mins[i][0]
                        k_idx = mins[i][1]

                lists[k_idx] = lists[k_idx].next

                n = ListNode(min_val)
                if head is None:
                    head = n
                    tail = n
                else:
                    tail.next = n
                    tail = n
            else:
                done = True

        return head
