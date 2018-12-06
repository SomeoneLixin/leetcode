# 第一种简单方法
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 第二种hash表
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        d = {}
        for i, item in enumerate(nums):
            tmp = target - item

            for key, value in d.items():
                if value == tmp:
                    return [key, i]

            d[i] = item

        return None
