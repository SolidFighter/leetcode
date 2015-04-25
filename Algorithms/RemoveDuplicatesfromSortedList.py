# Remove Duplicates from Sorted List Total Accepted: 55170 Total Submissions: 160848
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

__author__ = 'myang'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        curNode = head
        while curNode != None and curNode.next != None:
            if curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return head