__author__ = 'myang'

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in dict.values():
                stack.append(c)
            elif c in dict.keys():
                if stack == [] or stack.pop() != dict[c]:
                    return False
            else:
                return False

        return stack == []


