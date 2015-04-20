__author__ = 'myang'

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        A[:] = filter(lambda x: x != elem, A)
        return len(A)

if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 1, 3]
    ele = 1
    len = solution.removeElement(A, 1)
    print(A)
    print(len)
