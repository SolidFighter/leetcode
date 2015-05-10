__author__ = 'myang'

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        left_left, left = 0, 1

        for i in range(n):
            left_left, left = left, left_left + left
        return left


