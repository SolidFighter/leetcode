# Remove Nth Node From End of List Total Accepted: 49711 Total Submissions: 179621
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.

__author__ = 'myang'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        h = tail = head
        for i in range(n):
            tail = tail.next
        if tail == None:
            return head.next
        tail = tail.next
        while tail != None:
            tail = tail.next
            h = h.next
        h.next = h.next.next
        return head


