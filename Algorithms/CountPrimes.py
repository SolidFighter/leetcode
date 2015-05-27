__author__ = 'myang'


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2:
            return 0
        flag = [True] * n
        flag[0], flag[1] = False, False
        i = 2
        while i * i < n:
            if flag[i]:
                j = i
                while j * i < n:
                    flag[j * i] = False
                    j += 1
            i += 1
        return sum(flag)