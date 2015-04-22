# Pascal's Triangle
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


__author__ = 'myang'


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        lists = []
        for i in range(numRows):
            lists.append([1] * (i + 1))
            if i > 1:
                for j in range(1, i):
                    lists[i][j] = lists[i-1][j] + lists[i-1][j-1]
        return lists

if __name__ == '__main__':
    solution = Solution()
    numRows = 5
    triangle = solution.generate(numRows)
    print(triangle)