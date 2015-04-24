# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space? 

__author__ = 'myang'

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        pascal = [1, 1]
        for i in range(1, rowIndex):
            for j in range(0, i):
                pascal[j] = pascal[j] + pascal[j+1]
            pascal.insert(0, 1)
        return pascal

if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(2))

