# Rotate Array
#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Related problem: Reverse Words in a String II
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.


__author__ = 'myang'

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for i in range(start, int((start + end) / 2)):
            nums[i], nums[start + end - i - 1] = nums[start + end - i - 1], nums[i]

if __name__ == '__main__':
    solusion = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solusion.rotate(nums, 3)
    print(nums)