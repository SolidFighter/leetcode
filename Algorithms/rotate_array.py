__author__ = 'myang'

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        if n > 0 and k > 0:
            nums[:] = nums[n-k : ] + nums[ : n-k]

if __name__ == '__main__':
    solusion = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solusion.rotate(nums, 3)
    print(nums)