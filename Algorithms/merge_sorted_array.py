# Merge Sorted Array
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.



__author__ = 'myang'


class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1

if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 9, 0, 0, 0]
    B = [4, 5, 6]
    solution.merge(A, 3, B, 3)
    print(A)