# Merge Two Sorted Lists Total Accepted: 54260 Total Submissions: 165317
#
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

__author__ = 'myang'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        guardNode = ListNode(-1)
        node = guardNode
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        return guardNode.next