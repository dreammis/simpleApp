class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for index2 in range(len(nums))[index+1:]:
                if nums[index] + nums[index2] == target:
                    return [index, index2]

    def twoSum2(self, nums, target):
        # nums.sort()
        d = {}
        for index, value in enumerate(nums):
            if target - value in d:
                return [d[target-value], index]
            d[value] = index

solution = Solution()
print solution.twoSum2([3, 2, 9, 5, 10, 6], 14)
