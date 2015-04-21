# Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2]

__author__ = 'myang'

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 1:
            return len(A)
        cnt = 0
        for i in range(1, len(A)):
            if A[cnt] != A[i]:
                cnt += 1
                A[cnt] = A[i]
        return cnt + 1

if __name__ == '__main__':
    A = [1, 1, 2, 3, 3, 5]
    solution = Solution()
    len = solution.removeDuplicates(A)
    print(len)
    print(A)
