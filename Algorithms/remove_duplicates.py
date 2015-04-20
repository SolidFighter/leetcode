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
