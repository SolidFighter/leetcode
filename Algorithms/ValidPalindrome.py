__author__ = 'myang'

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]


