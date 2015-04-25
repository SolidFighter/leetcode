# Remove Linked List Elements Total Accepted: 3390 Total Submissions: 12228
#
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

__author__ = 'myang'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        tmp_head = ListNode(-1)
        tmp_head.next = head
        cur_node = tmp_head
        while cur_node != None and cur_node.next != None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return tmp_head.next
