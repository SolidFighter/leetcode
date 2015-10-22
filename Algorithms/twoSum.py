__author__ = 'myang'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i + 1
            else:
                return map[nums[i]], i + 1

if __name__ == '__main__':
    solution = Solution()
    i1, i2 = solution.twoSum([1, 3, 3], 6)
    print(i1, i2)
