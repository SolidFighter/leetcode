__author__ = 'myang'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        left_left, left = 0, 0
        for i in range(len(nums)):
            left_left, left = left, max(nums[i] + left_left, left)
        return left


